// ESBE Main JavaScript File
(function() {
    'use strict';

    // DOM Ready
    document.addEventListener('DOMContentLoaded', function() {
        initializeApp();
    });

    // Initialize Application
    function initializeApp() {
        initializeAnimations();
        initializeFormValidation();
        initializeTooltips();
        initializeScrollEffects();
        initializeLoadingStates();
        initializeSearchAndFilter();
        initializeProgrammeInteractions();
        initializeContactForm();
        initializeAccessibility();
    }

    // Animation System
    function initializeAnimations() {
        // Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        // Observe elements with animation classes
        document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(function(el) {
            observer.observe(el);
        });

        // Stagger animations for cards
        const cards = document.querySelectorAll('.card');
        cards.forEach(function(card, index) {
            card.style.animationDelay = (index * 0.1) + 's';
        });
    }

    // Form Validation
    function initializeFormValidation() {
        const forms = document.querySelectorAll('form');
        
        forms.forEach(function(form) {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                    showFormErrors(form);
                } else {
                    showLoadingState(form);
                }
                form.classList.add('was-validated');
            });

            // Real-time validation
            const inputs = form.querySelectorAll('input, select, textarea');
            inputs.forEach(function(input) {
                input.addEventListener('blur', function() {
                    validateField(input);
                });

                input.addEventListener('input', function() {
                    if (input.classList.contains('is-invalid')) {
                        validateField(input);
                    }
                });
            });
        });
    }

    // Validate individual field
    function validateField(field) {
        const isValid = field.checkValidity();
        
        if (isValid) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
            hideFieldError(field);
        } else {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
            showFieldError(field);
        }
    }

    // Show field error
    function showFieldError(field) {
        const errorDiv = field.parentNode.querySelector('.invalid-feedback') || 
                        createErrorElement(field);
        
        errorDiv.textContent = getFieldErrorMessage(field);
        errorDiv.style.display = 'block';
    }

    // Hide field error
    function hideFieldError(field) {
        const errorDiv = field.parentNode.querySelector('.invalid-feedback');
        if (errorDiv) {
            errorDiv.style.display = 'none';
        }
    }

    // Create error element
    function createErrorElement(field) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        field.parentNode.appendChild(errorDiv);
        return errorDiv;
    }

    // Get field error message
    function getFieldErrorMessage(field) {
        if (field.validity.valueMissing) {
            return 'This field is required.';
        }
        if (field.validity.typeMismatch) {
            return 'Please enter a valid ' + field.type + '.';
        }
        if (field.validity.tooShort) {
            return 'Please enter at least ' + field.minLength + ' characters.';
        }
        if (field.validity.tooLong) {
            return 'Please enter no more than ' + field.maxLength + ' characters.';
        }
        if (field.validity.patternMismatch) {
            return 'Please match the requested format.';
        }
        return 'Please enter a valid value.';
    }

    // Show form errors
    function showFormErrors(form) {
        const firstInvalidField = form.querySelector('.is-invalid');
        if (firstInvalidField) {
            firstInvalidField.focus();
            firstInvalidField.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // Initialize Tooltips
    function initializeTooltips() {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        if (window.bootstrap && window.bootstrap.Tooltip) {
            tooltipTriggerList.forEach(function(tooltipTriggerEl) {
                new bootstrap.Tooltip(tooltipTriggerEl);
            });
        }
    }

    // Scroll Effects
    function initializeScrollEffects() {
        // Navbar background change on scroll
        const navbar = document.querySelector('.navbar');
        if (navbar) {
            window.addEventListener('scroll', function() {
                if (window.scrollY > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }
            });
        }

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Back to top button
        createBackToTopButton();
    }

    // Create back to top button
    function createBackToTopButton() {
        const backToTop = document.createElement('button');
        backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
        backToTop.className = 'btn btn-primary position-fixed';
        backToTop.style.cssText = `
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: none;
            opacity: 0.8;
            transition: all 0.3s ease;
        `;
        backToTop.setAttribute('aria-label', 'Back to top');
        document.body.appendChild(backToTop);

        // Show/hide based on scroll position
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTop.style.display = 'block';
            } else {
                backToTop.style.display = 'none';
            }
        });

        // Scroll to top on click
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Loading States
    function initializeLoadingStates() {
        // Add loading state to forms
        document.querySelectorAll('form').forEach(function(form) {
            form.addEventListener('submit', function() {
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn && form.checkValidity()) {
                    showLoadingState(submitBtn);
                }
            });
        });
    }

    // Show loading state
    function showLoadingState(element) {
        if (element.tagName === 'FORM') {
            const submitBtn = element.querySelector('button[type="submit"]');
            if (submitBtn) {
                showLoadingState(submitBtn);
            }
        } else {
            element.classList.add('loading');
            element.disabled = true;
            
            // Store original text
            if (!element.dataset.originalText) {
                element.dataset.originalText = element.textContent;
            }
            
            // Add loading text
            element.innerHTML = '<span class="spinner me-2"></span>Processing...';
        }
    }

    // Hide loading state
    function hideLoadingState(element) {
        element.classList.remove('loading');
        element.disabled = false;
        
        if (element.dataset.originalText) {
            element.textContent = element.dataset.originalText;
        }
    }

    // Search and Filter
    function initializeSearchAndFilter() {
        const searchInput = document.querySelector('#programme-search');
        const filterSelects = document.querySelectorAll('.filter-select');
        const programmeCards = document.querySelectorAll('.programme-card');

        if (searchInput) {
            searchInput.addEventListener('input', debounce(handleSearch, 300));
        }

        filterSelects.forEach(function(select) {
            select.addEventListener('change', handleFilter);
        });

        function handleSearch() {
            const searchTerm = searchInput.value.toLowerCase();
            
            programmeCards.forEach(function(card) {
                const title = card.querySelector('.card-title').textContent.toLowerCase();
                const description = card.querySelector('.card-text').textContent.toLowerCase();
                const isMatch = title.includes(searchTerm) || description.includes(searchTerm);
                
                if (isMatch) {
                    card.closest('.col-lg-6, .col-xl-4').style.display = 'block';
                } else {
                    card.closest('.col-lg-6, .col-xl-4').style.display = 'none';
                }
            });

            updateResultsCount();
        }

        function handleFilter() {
            // This would be expanded based on specific filter requirements
            updateResultsCount();
        }

        function updateResultsCount() {
            const visibleCards = Array.from(programmeCards).filter(function(card) {
                return card.closest('.col-lg-6, .col-xl-4').style.display !== 'none';
            });

            const countElement = document.querySelector('.results-count');
            if (countElement) {
                countElement.textContent = visibleCards.length + ' programme' + 
                    (visibleCards.length !== 1 ? 's' : '') + ' found';
            }
        }
    }

    // Programme Interactions
    function initializeProgrammeInteractions() {
        // Add to favorites (local storage)
        document.querySelectorAll('.favorite-btn').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                toggleFavorite(this);
            });
        });

        // Programme comparison
        document.querySelectorAll('.compare-btn').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                toggleComparison(this);
            });
        });

        // Quick preview modals
        document.querySelectorAll('.quick-preview-btn').forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                showQuickPreview(this.dataset.programmeId);
            });
        });
    }

    // Toggle favorite
    function toggleFavorite(btn) {
        const programmeId = btn.dataset.programmeId;
        const favorites = JSON.parse(localStorage.getItem('esbe_favorites') || '[]');
        
        const index = favorites.indexOf(programmeId);
        if (index > -1) {
            favorites.splice(index, 1);
            btn.innerHTML = '<i class="far fa-heart"></i>';
            btn.classList.remove('active');
        } else {
            favorites.push(programmeId);
            btn.innerHTML = '<i class="fas fa-heart"></i>';
            btn.classList.add('active');
        }
        
        localStorage.setItem('esbe_favorites', JSON.stringify(favorites));
        showToast('Favorites updated', 'success');
    }

    // Toggle comparison
    function toggleComparison(btn) {
        const programmeId = btn.dataset.programmeId;
        const comparison = JSON.parse(localStorage.getItem('esbe_comparison') || '[]');
        
        if (comparison.length >= 3 && !comparison.includes(programmeId)) {
            showToast('You can only compare up to 3 programmes', 'warning');
            return;
        }
        
        const index = comparison.indexOf(programmeId);
        if (index > -1) {
            comparison.splice(index, 1);
            btn.classList.remove('active');
        } else {
            comparison.push(programmeId);
            btn.classList.add('active');
        }
        
        localStorage.setItem('esbe_comparison', JSON.stringify(comparison));
        updateComparisonCounter();
    }

    // Update comparison counter
    function updateComparisonCounter() {
        const comparison = JSON.parse(localStorage.getItem('esbe_comparison') || '[]');
        const counter = document.querySelector('.comparison-counter');
        
        if (counter) {
            counter.textContent = comparison.length;
            counter.style.display = comparison.length > 0 ? 'inline' : 'none';
        }
    }

    // Contact Form Enhancements
    function initializeContactForm() {
        const contactForm = document.querySelector('#contact-form');
        if (!contactForm) return;

        // Auto-populate programme field from URL
        const urlParams = new URLSearchParams(window.location.search);
        const programme = urlParams.get('programme');
        if (programme) {
            const programmeSelect = contactForm.querySelector('select[name="programme_interest"]');
            if (programmeSelect) {
                programmeSelect.value = programme;
            }
        }

        // Character counter for message field
        const messageField = contactForm.querySelector('textarea[name="message"]');
        if (messageField) {
            addCharacterCounter(messageField, 500);
        }

        // Phone number formatting
        const phoneField = contactForm.querySelector('input[name="phone"]');
        if (phoneField) {
            phoneField.addEventListener('input', formatPhoneNumber);
        }
    }

    // Add character counter
    function addCharacterCounter(field, maxLength) {
        const counter = document.createElement('small');
        counter.className = 'text-muted character-counter';
        field.parentNode.appendChild(counter);

        function updateCounter() {
            const remaining = maxLength - field.value.length;
            counter.textContent = remaining + ' characters remaining';
            
            if (remaining < 50) {
                counter.className = 'text-warning character-counter';
            } else if (remaining < 0) {
                counter.className = 'text-danger character-counter';
            } else {
                counter.className = 'text-muted character-counter';
            }
        }

        field.addEventListener('input', updateCounter);
        updateCounter();
    }

    // Format phone number
    function formatPhoneNumber(e) {
        const input = e.target;
        const value = input.value.replace(/\D/g, '');
        
        if (value.length <= 10) {
            input.value = value.replace(/(\d{3})(\d{3})(\d{4})/, '$1-$2-$3');
        } else {
            input.value = value.replace(/(\d{3})(\d{3})(\d{4})(\d+)/, '+$4-$1-$2-$3');
        }
    }

    // Accessibility Enhancements
    function initializeAccessibility() {
        // Skip to main content
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.className = 'skip-link';
        skipLink.textContent = 'Skip to main content';
        document.body.insertBefore(skipLink, document.body.firstChild);

        // Add main content landmark
        const main = document.querySelector('main');
        if (main) {
            main.id = 'main-content';
            main.setAttribute('tabindex', '-1');
        }

        // Keyboard navigation for cards
        document.querySelectorAll('.card').forEach(function(card) {
            card.setAttribute('tabindex', '0');
            card.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    const link = card.querySelector('a');
                    if (link) {
                        link.click();
                    }
                }
            });
        });

        // Announce dynamic content changes
        const liveRegion = document.createElement('div');
        liveRegion.setAttribute('aria-live', 'polite');
        liveRegion.setAttribute('aria-atomic', 'true');
        liveRegion.className = 'sr-only';
        liveRegion.id = 'live-region';
        document.body.appendChild(liveRegion);

        // High contrast mode detection
        if (window.matchMedia('(prefers-contrast: high)').matches) {
            document.body.classList.add('high-contrast');
        }

        // Reduced motion detection
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            document.body.classList.add('reduced-motion');
        }
    }

    // Utility Functions
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    function showToast(message, type = 'info') {
        const toastContainer = document.querySelector('.toast-container') || createToastContainer();
        const toast = createToast(message, type);
        toastContainer.appendChild(toast);

        // Auto-remove after 5 seconds
        setTimeout(function() {
            toast.remove();
        }, 5000);
    }

    function createToastContainer() {
        const container = document.createElement('div');
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '1055';
        document.body.appendChild(container);
        return container;
    }

    function createToast(message, type) {
        const toast = document.createElement('div');
        toast.className = `alert alert-${type} alert-dismissible fade show`;
        toast.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        return toast;
    }

    function announceToScreenReader(message) {
        const liveRegion = document.getElementById('live-region');
        if (liveRegion) {
            liveRegion.textContent = message;
        }
    }

    // Make functions available globally if needed
    window.ESBE = {
        showLoadingState: showLoadingState,
        hideLoadingState: hideLoadingState,
        showToast: showToast,
        announceToScreenReader: announceToScreenReader
    };

})();

// Additional Journey Builder Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Journey Builder specific code
    const journeyForm = document.getElementById('journey-form');
    if (journeyForm) {
        initializeJourneyBuilder();
    }
});

function initializeJourneyBuilder() {
    // Progress tracking
    const steps = document.querySelectorAll('.form-step');
    const progressBar = document.querySelector('.progress-bar');
    let currentStep = 1;

    // Update progress bar
    function updateProgress() {
        const progress = (currentStep / steps.length) * 100;
        if (progressBar) {
            progressBar.style.width = progress + '%';
        }
    }

    // Validate step
    function validateStep(stepNumber) {
        const step = document.getElementById(`step-${stepNumber}`);
        const requiredFields = step.querySelectorAll('[required]');
        let isValid = true;

        requiredFields.forEach(function(field) {
            if (!field.checkValidity()) {
                isValid = false;
                field.classList.add('is-invalid');
            } else {
                field.classList.remove('is-invalid');
            }
        });

        // Check radio button groups
        const radioGroups = {};
        step.querySelectorAll('input[type="radio"]').forEach(function(radio) {
            if (!radioGroups[radio.name]) {
                radioGroups[radio.name] = false;
            }
            if (radio.checked) {
                radioGroups[radio.name] = true;
            }
        });

        for (const groupName in radioGroups) {
            if (!radioGroups[groupName]) {
                isValid = false;
                break;
            }
        }

        return isValid;
    }

    // Save progress to localStorage
    function saveProgress() {
        const formData = new FormData(document.getElementById('journey-form'));
        const data = {};
        
        for (let [key, value] of formData.entries()) {
            if (data[key]) {
                if (Array.isArray(data[key])) {
                    data[key].push(value);
                } else {
                    data[key] = [data[key], value];
                }
            } else {
                data[key] = value;
            }
        }
        
        localStorage.setItem('esbe_journey_progress', JSON.stringify(data));
    }

    // Load progress from localStorage
    function loadProgress() {
        const savedData = localStorage.getItem('esbe_journey_progress');
        if (savedData) {
            const data = JSON.parse(savedData);
            
            Object.keys(data).forEach(function(key) {
                const field = document.querySelector(`[name="${key}"]`);
                if (field) {
                    if (field.type === 'radio' || field.type === 'checkbox') {
                        const fields = document.querySelectorAll(`[name="${key}"]`);
                        fields.forEach(function(f) {
                            if (Array.isArray(data[key])) {
                                f.checked = data[key].includes(f.value);
                            } else {
                                f.checked = f.value === data[key];
                            }
                        });
                    } else {
                        field.value = data[key];
                    }
                }
            });
        }
    }

    // Initialize
    updateProgress();
    loadProgress();

    // Save progress on form change
    document.getElementById('journey-form').addEventListener('change', saveProgress);

    // Clear saved progress on successful submission
    document.getElementById('journey-form').addEventListener('submit', function() {
        if (this.checkValidity()) {
            localStorage.removeItem('esbe_journey_progress');
        }
    });
}

// Programme filtering enhancements
function enhanceProgrammeFiltering() {
    const programmeCards = document.querySelectorAll('.programme-card');
    const filterButtons = document.querySelectorAll('.filter-btn');

    filterButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const filterValue = this.dataset.filter;
            
            // Update active state
            filterButtons.forEach(function(b) {
                b.classList.remove('active');
            });
            this.classList.add('active');

            // Filter programmes
            programmeCards.forEach(function(card) {
                const cardData = card.dataset;
                const shouldShow = filterValue === 'all' || 
                                  cardData.category === filterValue || 
                                  cardData.industry === filterValue;

                if (shouldShow) {
                    card.closest('.col-lg-6, .col-xl-4').style.display = 'block';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                } else {
                    card.closest('.col-lg-6, .col-xl-4').style.display = 'none';
                }
            });

            // Update results count
            const visibleCount = Array.from(programmeCards).filter(function(card) {
                return card.closest('.col-lg-6, .col-xl-4').style.display !== 'none';
            }).length;

            window.ESBE?.announceToScreenReader(`Showing ${visibleCount} programmes`);
        });
    });
}

// Initialize enhanced filtering if elements exist
document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.filter-btn')) {
        enhanceProgrammeFiltering();
    }
});
