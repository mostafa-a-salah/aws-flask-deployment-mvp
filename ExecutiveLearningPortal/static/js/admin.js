// Admin Dashboard JavaScript
(function() {
    'use strict';

    // Initialize admin dashboard
    document.addEventListener('DOMContentLoaded', function() {
        initializeAdmin();
    });

    function initializeAdmin() {
        initializeMediaUpload();
        initializeContentEditor();
        initializeFormValidation();
        initializeTooltips();
        initializeModals();
        initializeDataTables();
        initializeColorPickers();
        initializeDragAndDrop();
    }

    // Media Upload Functionality
    function initializeMediaUpload() {
        const uploadArea = document.querySelector('.media-upload-area');
        const fileInput = document.querySelector('#media-file-input');
        
        if (uploadArea && fileInput) {
            // Click to upload
            uploadArea.addEventListener('click', function() {
                fileInput.click();
            });

            // Drag and drop
            uploadArea.addEventListener('dragover', function(e) {
                e.preventDefault();
                this.classList.add('dragover');
            });

            uploadArea.addEventListener('dragleave', function(e) {
                e.preventDefault();
                this.classList.remove('dragover');
            });

            uploadArea.addEventListener('drop', function(e) {
                e.preventDefault();
                this.classList.remove('dragover');
                
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    handleFileUpload(files[0]);
                }
            });

            // File input change
            fileInput.addEventListener('change', function() {
                if (this.files.length > 0) {
                    handleFileUpload(this.files[0]);
                }
            });
        }
    }

    function handleFileUpload(file) {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('description', '');

        // Show loading state
        showLoadingState();

        fetch('/admin/media/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            hideLoadingState();
            if (data.success) {
                showNotification('File uploaded successfully!', 'success');
                // Refresh media grid or add new item
                location.reload();
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(error => {
            hideLoadingState();
            showNotification('Upload failed: ' + error.message, 'error');
        });
    }

    // Content Editor
    function initializeContentEditor() {
        const textareas = document.querySelectorAll('.content-editor');
        
        textareas.forEach(textarea => {
            // Add basic formatting toolbar
            const toolbar = createEditorToolbar();
            textarea.parentNode.insertBefore(toolbar, textarea);
            
            // Auto-resize
            textarea.addEventListener('input', function() {
                this.style.height = 'auto';
                this.style.height = this.scrollHeight + 'px';
            });
        });
    }

    function createEditorToolbar() {
        const toolbar = document.createElement('div');
        toolbar.className = 'editor-toolbar mb-2';
        toolbar.innerHTML = `
            <div class="btn-group btn-group-sm" role="group">
                <button type="button" class="btn btn-outline-secondary" onclick="formatText('bold')">
                    <i class="fas fa-bold"></i>
                </button>
                <button type="button" class="btn btn-outline-secondary" onclick="formatText('italic')">
                    <i class="fas fa-italic"></i>
                </button>
                <button type="button" class="btn btn-outline-secondary" onclick="formatText('underline')">
                    <i class="fas fa-underline"></i>
                </button>
            </div>
        `;
        return toolbar;
    }

    // Form Validation
    function initializeFormValidation() {
        const forms = document.querySelectorAll('form');
        
        forms.forEach(form => {
            form.addEventListener('submit', function(e) {
                if (!form.checkValidity()) {
                    e.preventDefault();
                    e.stopPropagation();
                    showFormErrors(form);
                }
                form.classList.add('was-validated');
            });

            // Real-time validation
            const inputs = form.querySelectorAll('input, select, textarea');
            inputs.forEach(input => {
                input.addEventListener('blur', function() {
                    validateField(this);
                });
            });
        });
    }

    function validateField(field) {
        const isValid = field.checkValidity();
        
        if (isValid) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
        } else {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
        }
    }

    function showFormErrors(form) {
        const firstInvalid = form.querySelector('.is-invalid, :invalid');
        if (firstInvalid) {
            firstInvalid.focus();
            firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // Tooltips
    function initializeTooltips() {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        if (window.bootstrap && window.bootstrap.Tooltip) {
            tooltipTriggerList.forEach(function(tooltipTriggerEl) {
                new bootstrap.Tooltip(tooltipTriggerEl);
            });
        }
    }

    // Modals
    function initializeModals() {
        // Auto-focus first input in modals
        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('shown.bs.modal', function() {
                const firstInput = this.querySelector('input, select, textarea');
                if (firstInput) {
                    firstInput.focus();
                }
            });
        });
    }

    // Data Tables Enhancement
    function initializeDataTables() {
        const tables = document.querySelectorAll('.data-table');
        
        tables.forEach(table => {
            // Add search functionality
            addTableSearch(table);
            
            // Add sorting
            addTableSorting(table);
            
            // Add row selection
            addRowSelection(table);
        });
    }

    function addTableSearch(table) {
        const searchInput = document.createElement('input');
        searchInput.type = 'text';
        searchInput.className = 'form-control mb-3';
        searchInput.placeholder = 'Search...';
        
        table.parentNode.insertBefore(searchInput, table);
        
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const rows = table.querySelectorAll('tbody tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    }

    function addTableSorting(table) {
        const headers = table.querySelectorAll('thead th');
        
        headers.forEach((header, index) => {
            header.style.cursor = 'pointer';
            header.addEventListener('click', function() {
                sortTable(table, index);
            });
        });
    }

    function sortTable(table, columnIndex) {
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));
        
        const isAscending = !table.dataset.sortAsc || table.dataset.sortAsc === 'false';
        
        rows.sort((a, b) => {
            const aText = a.cells[columnIndex].textContent.trim();
            const bText = b.cells[columnIndex].textContent.trim();
            
            if (isAscending) {
                return aText.localeCompare(bText);
            } else {
                return bText.localeCompare(aText);
            }
        });
        
        rows.forEach(row => tbody.appendChild(row));
        table.dataset.sortAsc = isAscending;
    }

    function addRowSelection(table) {
        const rows = table.querySelectorAll('tbody tr');
        
        rows.forEach(row => {
            row.addEventListener('click', function(e) {
                if (e.target.tagName !== 'A' && e.target.tagName !== 'BUTTON') {
                    this.classList.toggle('table-active');
                }
            });
        });
    }

    // Color Pickers
    function initializeColorPickers() {
        const colorInputs = document.querySelectorAll('input[type="color"]');
        
        colorInputs.forEach(input => {
            // Add color preview
            const preview = document.createElement('div');
            preview.className = 'color-preview';
            preview.style.cssText = `
                width: 30px;
                height: 30px;
                border-radius: 50%;
                border: 2px solid #ddd;
                display: inline-block;
                margin-left: 10px;
                vertical-align: middle;
                background-color: ${input.value};
            `;
            
            input.parentNode.appendChild(preview);
            
            input.addEventListener('change', function() {
                preview.style.backgroundColor = this.value;
            });
        });
    }

    // Drag and Drop for Reordering
    function initializeDragAndDrop() {
        const sortableLists = document.querySelectorAll('.sortable-list');
        
        sortableLists.forEach(list => {
            new Sortable(list, {
                animation: 150,
                ghostClass: 'sortable-ghost',
                onEnd: function(evt) {
                    updateOrder(list);
                }
            });
        });
    }

    function updateOrder(list) {
        const items = list.querySelectorAll('[data-id]');
        const order = Array.from(items).map(item => item.dataset.id);
        
        // Send order update to server
        fetch('/admin/update-order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ order: order })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('Order updated successfully!', 'success');
            }
        });
    }

    // Utility Functions
    function showLoadingState() {
        const loader = document.createElement('div');
        loader.id = 'global-loader';
        loader.className = 'position-fixed top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center';
        loader.style.cssText = 'background: rgba(0,0,0,0.5); z-index: 9999;';
        loader.innerHTML = `
            <div class="spinner-border text-light" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        `;
        document.body.appendChild(loader);
    }

    function hideLoadingState() {
        const loader = document.getElementById('global-loader');
        if (loader) {
            loader.remove();
        }
    }

    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    // Global functions
    window.formatText = function(command) {
        document.execCommand(command, false, null);
    };

    window.insertMedia = function(url) {
        const activeTextarea = document.activeElement;
        if (activeTextarea && activeTextarea.tagName === 'TEXTAREA') {
            const cursorPos = activeTextarea.selectionStart;
            const textBefore = activeTextarea.value.substring(0, cursorPos);
            const textAfter = activeTextarea.value.substring(cursorPos);
            
            activeTextarea.value = textBefore + `![Image](${url})` + textAfter;
            activeTextarea.focus();
        }
    };

    window.confirmDelete = function(message = 'Are you sure you want to delete this item?') {
        return confirm(message);
    };

    // Export functions for global use
    window.AdminDashboard = {
        showNotification: showNotification,
        showLoadingState: showLoadingState,
        hideLoadingState: hideLoadingState,
        validateField: validateField
    };

})();

// Media Library Modal
function openMediaLibrary(callback) {
    fetch('/admin/api/media-list')
        .then(response => response.json())
        .then(data => {
            showMediaLibraryModal(data, callback);
        });
}

function showMediaLibraryModal(mediaFiles, callback) {
    const modal = document.createElement('div');
    modal.className = 'modal fade';
    modal.innerHTML = `
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Media Library</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <div class="row g-3">
                        ${mediaFiles.map(file => `
                            <div class="col-md-3">
                                <div class="card media-item" onclick="selectMedia('${file.url}', '${file.filename}')">
                                    <img src="${file.url}" class="card-img-top" alt="${file.filename}">
                                    <div class="card-body p-2">
                                        <small class="text-muted">${file.filename}</small>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    const bsModal = new bootstrap.Modal(modal);
    bsModal.show();
    
    modal.addEventListener('hidden.bs.modal', function() {
        modal.remove();
    });
    
    window.selectMedia = function(url, filename) {
        if (callback) {
            callback(url, filename);
        }
        bsModal.hide();
    };
}

// Programme Module Management
function addModule() {
    const moduleContainer = document.getElementById('modules-container');
    const moduleCount = moduleContainer.children.length;
    
    const moduleDiv = document.createElement('div');
    moduleDiv.className = 'input-group mb-2';
    moduleDiv.innerHTML = `
        <input type="text" name="module_${moduleCount}" class="form-control" placeholder="Module ${moduleCount + 1}">
        <button type="button" class="btn btn-outline-danger" onclick="removeModule(this)">
            <i class="fas fa-trash"></i>
        </button>
    `;
    
    moduleContainer.appendChild(moduleDiv);
    document.getElementById('module-count').value = moduleCount + 1;
}

function removeModule(button) {
    button.parentElement.remove();
    updateModuleCount();
}

function updateModuleCount() {
    const moduleContainer = document.getElementById('modules-container');
    document.getElementById('module-count').value = moduleContainer.children.length;
}

// Auto-save functionality
let autoSaveTimer;

function enableAutoSave(formId) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    const inputs = form.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(() => {
                autoSave(form);
            }, 2000);
        });
    });
}

function autoSave(form) {
    const formData = new FormData(form);
    formData.append('auto_save', 'true');
    
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('Auto-saved', 'info');
        }
    })
    .catch(error => {
        console.log('Auto-save failed:', error);
    });
}