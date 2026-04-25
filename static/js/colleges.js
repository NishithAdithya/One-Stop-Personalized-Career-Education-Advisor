/**
 * Colleges Page Interaction
 * Handles college listing, filtering, and display
 */

let currentColleges = [];
let selectedColleges = [];
const MAX_COMPARISONS = 3;

document.addEventListener('DOMContentLoaded', async function () {
    initializeCollegesPage();
});

async function initializeCollegesPage() {
    console.log('Initializing colleges page...');
    await loadColleges();
    setupEventListeners();
    populateFilterOptions();
}

/**
 * Load and display all colleges
 */
async function loadColleges(filters = {}) {
    try {
        showLoadingState();
        const data = await API.getColleges(filters);

        if (data.error) {
            showError('Failed to load colleges: ' + data.error);
            return;
        }

        currentColleges = data.colleges || [];
        displayColleges(currentColleges);
        updateStats(data.total || currentColleges.length);
    } catch (error) {
        console.error('Error loading colleges:', error);
        showError('Error loading colleges');
    }
}

/**
 * Display colleges in grid format
 */
function displayColleges(colleges) {
    const container = document.getElementById('colleges-container');
    if (!container) return;

    if (!colleges || colleges.length === 0) {
        container.innerHTML = '<div class="no-results">No colleges found. Try adjusting your filters.</div>';
        return;
    }

    container.innerHTML = colleges.map((college, index) => `
    <div class="college-card" data-college-id="${college.id || index}">
      <div class="college-header">
        <h3 class="college-name">${college.name}</h3>
        <span class="college-type ${college.college_type.toLowerCase()}">${college.college_type}</span>
      </div>
      
      <div class="college-info">
        <p><strong>Location:</strong> ${college.city}, ${college.state}</p>
        <p><strong>Degree:</strong> ${college.degree_type}</p>
        <p><strong>Annual Fees:</strong> ₹${(college.total_fees || 0).toLocaleString('en-IN')}</p>
        <p><strong>Admission:</strong> ${college.admission_type}</p>
        ${college.cutoff_percentage ? `<p><strong>Cutoff:</strong> ${college.cutoff_percentage}%</p>` : ''}
      </div>
      
      ${college.branches && college.branches.length > 0 ? `
        <div class="branches">
          <strong>Branches:</strong>
          <div class="branch-tags">
            ${college.branches.slice(0, 3).map(b => `<span class="tag">${b}</span>`).join('')}
            ${college.branches.length > 3 ? `<span class="tag">+${college.branches.length - 3} more</span>` : ''}
          </div>
        </div>
      ` : ''}
      
      <div class="college-actions">
        <button class="btn btn-primary" onclick="viewCollege('${college.id || index}')">View Details</button>
        <button class="btn btn-secondary" onclick="toggleCompare('${college.id || index}')">
          <span class="compare-text">Compare</span>
        </button>
      </div>
    </div>
  `).join('');

    hideLoadingState();
}

/**
 * View college details in modal
 */
async function viewCollege(collegeId) {
    try {
        const college = currentColleges.find(c => c.id === collegeId || currentColleges.indexOf(c) === parseInt(collegeId));

        if (!college) {
            showError('College not found');
            return;
        }

        const modal = document.getElementById('college-modal');
        if (!modal) {
            createModal();
            return viewCollege(collegeId);
        }

        // Populate modal content
        document.getElementById('modal-name').textContent = college.name;
        document.getElementById('modal-type').textContent = college.college_type;
        document.getElementById('modal-city').textContent = college.city + ', ' + college.state;
        document.getElementById('modal-degree').textContent = college.degree_type;
        document.getElementById('modal-fees').textContent = '₹' + (college.total_fees || 0).toLocaleString('en-IN');
        document.getElementById('modal-admission').textContent = college.admission_type;
        document.getElementById('modal-established').textContent = college.established_year || 'N/A';
        document.getElementById('modal-affiliation').textContent = college.affiliation || 'N/A';

        if (college.branches && college.branches.length > 0) {
            document.getElementById('modal-branches').innerHTML = college.branches
                .map(b => `<li>${b}</li>`).join('');
        }

        if (college.facilities && college.facilities.length > 0) {
            document.getElementById('modal-facilities').innerHTML = college.facilities
                .map(f => `<li>${f}</li>`).join('');
        }

        if (college.website) {
            document.getElementById('modal-website').href = college.website;
            document.getElementById('modal-website').style.display = 'inline-block';
        }

        if (college.contact_email) {
            document.getElementById('modal-email').textContent = college.contact_email;
        }

        if (college.contact_phone) {
            document.getElementById('modal-phone').textContent = college.contact_phone;
        }

        modal.classList.add('active');
    } catch (error) {
        console.error('Error viewing college:', error);
        showError('Error loading college details');
    }
}

/**
 * Toggle college selection for comparison
 */
function toggleCompare(collegeId) {
    const college = currentColleges.find(c => c.id === collegeId || currentColleges.indexOf(c) === parseInt(collegeId));

    if (!college) return;

    const index = selectedColleges.findIndex(c => c.id === college.id);

    if (index > -1) {
        selectedColleges.splice(index, 1);
    } else {
        if (selectedColleges.length < MAX_COMPARISONS) {
            selectedColleges.push(college);
        } else {
            showError(`Maximum ${MAX_COMPARISONS} colleges can be compared`);
            return;
        }
    }

    updateCompareButton();

    if (selectedColleges.length > 0) {
        showComparePreview();
    } else {
        hideComparePreview();
    }
}

/**
 * Update compare button states
 */
function updateCompareButton() {
    document.querySelectorAll('.college-card').forEach(card => {
        const btn = card.querySelector('.btn-secondary');
        const collegeId = card.dataset.collegeId;
        const isSelected = selectedColleges.some(c => c.id === collegeId || currentColleges.indexOf(c) === parseInt(collegeId));

        if (isSelected) {
            btn.classList.add('active');
            btn.innerHTML = '<span class="compare-text">✓ Selected</span>';
        } else {
            btn.classList.remove('active');
            btn.innerHTML = '<span class="compare-text">Compare</span>';
        }
    });
}

/**
 * Show compare preview
 */
function showComparePreview() {
    let preview = document.getElementById('compare-preview');

    if (!preview) {
        preview = document.createElement('div');
        preview.id = 'compare-preview';
        preview.className = 'compare-preview';
        document.body.appendChild(preview);
    }

    preview.innerHTML = `
    <div class="compare-preview-content">
      <h4>Selected for Comparison (${selectedColleges.length}/${MAX_COMPARISONS})</h4>
      <div class="selected-colleges">
        ${selectedColleges.map((c, i) => `
          <span class="selected-tag">
            ${c.name}
            <button onclick="toggleCompare('${c.id || i}')" class="remove-tag">×</button>
          </span>
        `).join('')}
      </div>
      <button class="btn btn-primary" onclick="goToComparison()">
        Compare Now
      </button>
    </div>
  `;

    preview.classList.add('visible');
}

/**
 * Hide compare preview
 */
function hideComparePreview() {
    const preview = document.getElementById('compare-preview');
    if (preview) {
        preview.classList.remove('visible');
    }
}

/**
 * Go to comparison page
 */
function goToComparison() {
    if (selectedColleges.length === 0) {
        showError('Please select colleges to compare');
        return;
    }

    // Store selected colleges in sessionStorage for comparison page
    sessionStorage.setItem('compareColleges', JSON.stringify(selectedColleges));
    window.location.href = '/colleges/compare';
}

/**
 * Setup filter event listeners
 */
function setupEventListeners() {
    const searchBtn = document.getElementById('search-btn');
    if (searchBtn) {
        searchBtn.addEventListener('click', handleSearch);
    }

    const filterBtn = document.getElementById('filter-btn');
    if (filterBtn) {
        filterBtn.addEventListener('click', handleFilter);
    }

    const resetBtn = document.getElementById('reset-filters-btn');
    if (resetBtn) {
        resetBtn.addEventListener('click', resetFilters);
    }

    const closeModalBtn = document.querySelector('.close-modal');
    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    }

    // Close modal on outside click
    const modal = document.getElementById('college-modal');
    if (modal) {
        modal.addEventListener('click', function (e) {
            if (e.target === modal) closeModal();
        });
    }
}

/**
 * Handle search
 */
async function handleSearch() {
    const query = document.getElementById('search-input')?.value || '';

    if (!query.trim()) {
        showError('Please enter a search query');
        return;
    }

    try {
        showLoadingState();
        const data = await API.searchColleges(query);
        currentColleges = data.colleges || [];
        displayColleges(currentColleges);
    } catch (error) {
        console.error('Error searching:', error);
        showError('Search error');
    }
}

/**
 * Handle filter
 */
async function handleFilter() {
    const filters = {
        city: document.getElementById('filter-city')?.value || '',
        degree_type: document.getElementById('filter-degree')?.value || '',
        college_type: document.getElementById('filter-type')?.value || ''
    };

    // Remove empty filters
    Object.keys(filters).forEach(key => !filters[key] && delete filters[key]);

    await loadColleges(filters);
}

/**
 * Reset filters
 */
async function resetFilters() {
    document.getElementById('search-input').value = '';
    document.getElementById('filter-city').value = '';
    document.getElementById('filter-degree').value = '';
    document.getElementById('filter-type').value = '';

    selectedColleges = [];
    updateCompareButton();
    hideComparePreview();

    await loadColleges();
}

/**
 * Populate filter options
 */
async function populateFilterOptions() {
    try {
        const stats = await API.getStatistics();

        if (stats.by_city) {
            const citySelect = document.getElementById('filter-city');
            if (citySelect) {
                const cities = Object.keys(stats.by_city);
                citySelect.innerHTML = '<option value="">All Cities</option>' +
                    cities.map(city => `<option value="${city}">${city}</option>`).join('');
            }
        }
    } catch (error) {
        console.error('Error populating filters:', error);
    }
}

/**
 * Update statistics display
 */
function updateStats(total) {
    const statsElement = document.getElementById('colleges-stats');
    if (statsElement) {
        statsElement.textContent = `Showing ${currentColleges.length} of ${total} colleges`;
    }
}

/**
 * Create modal element
 */
function createModal() {
    const modal = document.createElement('div');
    modal.id = 'college-modal';
    modal.className = 'modal';
    modal.innerHTML = `
    <div class="modal-content">
      <span class="close-modal">&times;</span>
      <h2 id="modal-name"></h2>
      <span class="modal-type" id="modal-type"></span>
      
      <div class="modal-section">
        <h4>Basic Information</h4>
        <p><strong>Location:</strong> <span id="modal-city"></span></p>
        <p><strong>Degree:</strong> <span id="modal-degree"></span></p>
        <p><strong>College Type:</strong> <span id="modal-type"></span></p>
        <p><strong>Founded:</strong> <span id="modal-established"></span></p>
        <p><strong>Affiliation:</strong> <span id="modal-affiliation"></span></p>
      </div>
      
      <div class="modal-section">
        <h4>Admission Details</h4>
        <p><strong>Admission Type:</strong> <span id="modal-admission"></span></p>
        <p><strong>Annual Fees:</strong> <span id="modal-fees"></span></p>
      </div>
      
      <div class="modal-section">
        <h4>Programs</h4>
        <ul id="modal-branches"></ul>
      </div>
      
      <div class="modal-section">
        <h4>Facilities</h4>
        <ul id="modal-facilities"></ul>
      </div>
      
      <div class="modal-section">
        <h4>Contact</h4>
        <p><strong>Email:</strong> <span id="modal-email"></span></p>
        <p><strong>Phone:</strong> <span id="modal-phone"></span></p>
        <p><strong>Website:</strong> <a id="modal-website" target="_blank" style="display:none;"></a></p>
      </div>
    </div>
  `;

    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('.close-modal');
    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function (e) {
        if (e.target === modal) closeModal();
    });
}

/**
 * Close modal
 */
function closeModal() {
    const modal = document.getElementById('college-modal');
    if (modal) {
        modal.classList.remove('active');
    }
}

/**
 * Show loading state
 */
function showLoadingState() {
    const container = document.getElementById('colleges-container');
    if (container) {
        container.innerHTML = '<div class="loading">Loading colleges...</div>';
    }
}

/**
 * Hide loading state
 */
function hideLoadingState() {
    const loading = document.querySelector('.loading');
    if (loading) {
        loading.remove();
    }
}

/**
 * Show error message
 */
function showError(message) {
    console.error(message);
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    document.body.appendChild(errorDiv);

    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}
