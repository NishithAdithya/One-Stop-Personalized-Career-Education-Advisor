// ============ MODERNIZED COLLEGE-FOCUSED QUIZ DATA ============
// Questions designed to recommend the BEST college for each student

const quizData = [
    {
        id: 1,
        question: "What is your primary academic strength?",
        category: "Academic Foundation",
        options: [
            { text: "Physics, Mathematics & Chemistry (Strong in Science)", scores: { engineering: 5, science: 5, medicine: 5, commerce: 1, arts: 0 } },
            { text: "Biology & Chemistry (Life Sciences)", scores: { engineering: 2, science: 5, medicine: 5, commerce: 1, arts: 0 } },
            { text: "Economics, Commerce & Accounting", scores: { engineering: 0, science: 0, medicine: 0, commerce: 5, arts: 2 } },
            { text: "History, Literature & Languages", scores: { engineering: 0, science: 0, medicine: 0, commerce: 2, arts: 5 } }
        ]
    },
    {
        id: 2,
        question: "What type of college facility matters most to you?",
        category: "College Infrastructure",
        options: [
            { text: "Advanced labs, research facilities, and tech infrastructure", scores: { engineering: 5, science: 5, medicine: 4, commerce: 2, arts: 1 } },
            { text: "Practical workshops, hands-on training, and industry partnerships", scores: { engineering: 4, science: 3, medicine: 3, commerce: 3, arts: 2 } },
            { text: "Library, seminar halls, and classroom facilities", scores: { engineering: 2, science: 3, medicine: 3, commerce: 4, arts: 5 } },
            { text: "IT labs, computer facilities, and digital infrastructure", scores: { engineering: 5, science: 2, medicine: 2, commerce: 5, arts: 2 } }
        ]
    },
    {
        id: 3,
        question: "Which college type appeals to you most?",
        category: "College Preference",
        options: [
            { text: "IIT/NIT (Premium Engineering - highly competitive)", scores: { engineering: 5, science: 2, medicine: 2, commerce: 0, arts: 0 } },
            { text: "AIIMS/Medical Colleges (Medical Education)", scores: { engineering: 0, science: 4, medicine: 5, commerce: 0, arts: 0 } },
            { text: "Tier-1 Govt Colleges (Engineering/Science/Commerce)", scores: { engineering: 4, science: 4, medicine: 2, commerce: 4, arts: 3 } },
            { text: "General Govt College (Accessible, diverse programs)", scores: { engineering: 2, science: 3, medicine: 2, commerce: 4, arts: 4 } }
        ]
    },
    {
        id: 4,
        question: "What's your career aspirations after graduation?",
        category: "Career Goals",
        options: [
            { text: "Doctor, Engineer, or Scientist (Technical field)", scores: { engineering: 5, science: 5, medicine: 5, commerce: 0, arts: 0 } },
            { text: "IAS/IPS, Banker, or Business Executive", scores: { engineering: 1, science: 1, medicine: 0, commerce: 5, arts: 3 } },
            { text: "Lawyer, Journalist, or Government Officer", scores: { engineering: 0, science: 1, medicine: 0, commerce: 2, arts: 5 } },
            { text: "Entrepreneur or Self-employed professional", scores: { engineering: 4, science: 2, medicine: 1, commerce: 5, arts: 3 } }
        ]
    },
    {
        id: 5,
        question: "How important is your target college's ranking/reputation?",
        category: "College Selection Criteria",
        options: [
            { text: "Extremely important - Want top-ranked college only", scores: { engineering: 5, science: 4, medicine: 5, commerce: 4, arts: 3 } },
            { text: "Very important - Good rank preferred", scores: { engineering: 4, science: 4, medicine: 4, commerce: 4, arts: 4 } },
            { text: "Moderate - Decent college is fine", scores: { engineering: 3, science: 3, medicine: 2, commerce: 3, arts: 3 } },
            { text: "Not important - Any college with right course", scores: { engineering: 2, science: 2, medicine: 1, commerce: 2, arts: 2 } }
        ]
    },
    {
        id: 6,
        question: "What's your expected JEE/entrance exam performance level?",
        category: "Entrance Exam Readiness",
        options: [
            { text: "Excellent (95+ percentile expected) - IIT/AIIMS level", scores: { engineering: 5, science: 5, medicine: 5, commerce: 0, arts: 0 } },
            { text: "Good (80-95 percentile) - NIT/Tier-1 college", scores: { engineering: 4, science: 4, medicine: 4, commerce: 1, arts: 0 } },
            { text: "Moderate (60-80 percentile) - Govt college", scores: { engineering: 3, science: 3, medicine: 2, commerce: 3, arts: 1 } },
            { text: "Below average - Merit-based admission needed", scores: { engineering: 1, science: 1, medicine: 0, commerce: 2, arts: 2 } }
        ]
    },
    {
        id: 7,
        question: "What's your preferred location/state for college?",
        category: "Location Preference",
        options: [
            { text: "Big cities (Delhi, Bangalore, Mumbai, Hyderabad)", scores: { engineering: 5, science: 4, medicine: 4, commerce: 5, arts: 4 } },
            { text: "Home state or nearby region", scores: { engineering: 3, science: 3, medicine: 3, commerce: 3, arts: 3 } },
            { text: "Tier-2 cities (Pune, Jaipur, Lucknow, Chandigarh)", scores: { engineering: 4, science: 3, medicine: 3, commerce: 4, arts: 3 } },
            { text: "Doesn't matter - Education quality is key", scores: { engineering: 4, science: 4, medicine: 5, commerce: 4, arts: 4 } }
        ]
    },
    {
        id: 8,
        question: "How important is campus life and activities?",
        category: "College Experience",
        options: [
            { text: "Very important - Want vibrant campus with clubs/sports", scores: { engineering: 4, science: 3, medicine: 3, commerce: 4, arts: 5 } },
            { text: "Moderately important - Some social activities needed", scores: { engineering: 3, science: 3, medicine: 3, commerce: 3, arts: 4 } },
            { text: "Not very important - Focus on academics", scores: { engineering: 5, science: 5, medicine: 5, commerce: 3, arts: 2 } },
            { text: "Unsure - Want balanced experience", scores: { engineering: 3, science: 3, medicine: 3, commerce: 3, arts: 3 } }
        ]
    },
    {
        id: 9,
        question: "What are your placement expectations after college?",
        category: "Post-Graduation Plans",
        options: [
            { text: "High salary & MNC placement (₹10+ LPA expected)", scores: { engineering: 5, science: 2, medicine: 4, commerce: 5, arts: 1 } },
            { text: "Good salary & decent company (₹5-10 LPA)", scores: { engineering: 4, science: 3, medicine: 4, commerce: 4, arts: 2 } },
            { text: "Further education (Masters/PhD/Professional degree)", scores: { engineering: 3, science: 5, medicine: 5, commerce: 2, arts: 4 } },
            { text: "Flexible path - Entrepreneurship or civil services", scores: { engineering: 2, science: 2, medicine: 1, commerce: 4, arts: 4 } }
        ]
    },
    {
        id: 10,
        question: "How do you rank government colleges in your preference?",
        category: "College Preference Level",
        options: [
            { text: "Prefer only top govt colleges (IIT, NIT, AIIMS level)", scores: { engineering: 5, science: 5, medicine: 5, commerce: 4, arts: 3 } },
            { text: "Prefer govt colleges over private", scores: { engineering: 4, science: 4, medicine: 4, commerce: 4, arts: 4 } },
            { text: "Indifferent - Best education matters", scores: { engineering: 3, science: 3, medicine: 3, commerce: 3, arts: 3 } },
            { text: "Open to private if govt not possible", scores: { engineering: 2, science: 2, medicine: 2, commerce: 2, arts: 2 } }
        ]
    },
    {
        id: 11,
        question: "What's your financial situation for education?",
        category: "Financial Consideration",
        options: [
            { text: "No budget constraints - Best college is priority", scores: { engineering: 5, science: 4, medicine: 5, commerce: 5, arts: 4 } },
            { text: "Can afford premium colleges", scores: { engineering: 4, science: 4, medicine: 4, commerce: 4, arts: 4 } },
            { text: "Need affordable college - Fee is concern", scores: { engineering: 3, science: 3, medicine: 2, commerce: 3, arts: 3 } },
            { text: "Very limited budget - Scholarship required", scores: { engineering: 2, science: 2, medicine: 1, commerce: 2, arts: 2 } }
        ]
    },
    {
        id: 12,
        question: "Which statement best describes your college goal?",
        category: "Final College Goal",
        options: [
            { text: "Get into India's best college regardless of course", scores: { engineering: 5, science: 5, medicine: 5, commerce: 5, arts: 5 } },
            { text: "Find college that offers my preferred course well", scores: { engineering: 5, science: 5, medicine: 5, commerce: 4, arts: 4 } },
            { text: "Balance between college rank and course preference", scores: { engineering: 4, science: 4, medicine: 4, commerce: 4, arts: 4 } },
            { text: "Get any college with good educational value", scores: { engineering: 3, science: 3, medicine: 3, commerce: 3, arts: 3 } }
        ]
    }
];

// ============ QUIZ STATE ============
let currentIndex = 0;
let selectedAnswers = {};
let totalQuestions = quizData.length;

// ============ INITIALIZATION ============
document.addEventListener('DOMContentLoaded', function () {
    initializeQuiz();
});

function initializeQuiz() {
    // Initialize answers object
    quizData.forEach(q => {
        selectedAnswers[q.id] = null;
    });

    // Render first question
    renderQuestion(0);
    updateProgress();
}

// ============ QUIZ RENDERING ============
function renderQuestion(index) {
    const container = document.getElementById('quizContainer');
    container.innerHTML = '';

    const question = quizData[index];
    const questionDiv = document.createElement('div');
    questionDiv.className = 'quiz-question active';

    // Add category badge if available
    let categoryHTML = '';
    if (question.category) {
        categoryHTML = `<div style="display: inline-block; background: linear-gradient(135deg, #00d9ff, #4a90e2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.5px;">📌 ${question.category}</div>`;
    }

    let optionsHTML = `${categoryHTML}<h2>${question.question}</h2><div class="options-group">`;

    question.options.forEach((option, i) => {
        const isChecked = selectedAnswers[question.id] === i ? 'checked' : '';
        optionsHTML += `
            <label class="option-radio">
                <input 
                    type="radio" 
                    name="q${question.id}" 
                    value="${i}"
                    ${isChecked}
                    onchange="selectOption(${question.id}, ${i})"
                >
                <span class="option-label">${option.text}</span>
            </label>
        `;
    });

    optionsHTML += `</div>`;
    questionDiv.innerHTML = optionsHTML;
    container.appendChild(questionDiv);

    updateButtonStates();
}

function selectOption(questionId, optionIndex) {
    selectedAnswers[questionId] = optionIndex;
    updateProgress();
}

function updateProgress() {
    const answered = Object.values(selectedAnswers).filter(a => a !== null).length;
    const progress = (answered / totalQuestions) * 100;

    const progressFill = document.getElementById('progressFill');
    if (progressFill) {
        progressFill.style.width = progress + '%';
    }

    const currentQuestion = document.getElementById('currentQuestion');
    if (currentQuestion) {
        currentQuestion.textContent = currentIndex + 1;
    }

    const questionCounter = document.getElementById('questionCounter');
    if (questionCounter) {
        questionCounter.textContent = `Question ${currentIndex + 1} of ${totalQuestions}`;
    }

    const answeredCount = document.getElementById('answeredCount');
    if (answeredCount) {
        answeredCount.textContent = answered;
    }

    updateSidebar();
}

function updateSidebar() {
    document.querySelectorAll('.topic-item').forEach((item, index) => {
        if (index === currentIndex) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }

        if (selectedAnswers[quizData[index].id] !== null) {
            item.classList.add('completed');
        } else {
            item.classList.remove('completed');
        }
    });
}

function updateButtonStates() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');

    if (prevBtn) {
        prevBtn.disabled = currentIndex === 0;
    }

    if (currentIndex === totalQuestions - 1) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (submitBtn) submitBtn.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'block';
        if (submitBtn) submitBtn.style.display = 'none';
    }
}

// ============ NAVIGATION ============
function nextQuestion() {
    if (currentIndex < totalQuestions - 1) {
        currentIndex++;
        renderQuestion(currentIndex);
        updateProgress();
        document.getElementById('quizContainer').scrollIntoView({ behavior: 'smooth' });
    }
}

function previousQuestion() {
    if (currentIndex > 0) {
        currentIndex--;
        renderQuestion(currentIndex);
        updateProgress();
        document.getElementById('quizContainer').scrollIntoView({ behavior: 'smooth' });
    }
}

// ============ QUIZ SUBMISSION ============
document.getElementById('quizForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Check if all questions are answered
    const allAnswered = Object.values(selectedAnswers).every(a => a !== null);

    if (!allAnswered) {
        alert('Please answer all questions before submitting!');
        return;
    }

    submitQuiz();
});

function submitQuiz() {
    // Show loading message
    const quizContainer = document.getElementById('quizContainer');
    const quizForm = document.getElementById('quizForm');
    const quizSidebar = document.querySelector('.quiz-sidebar');

    if (quizContainer) quizContainer.style.display = 'none';
    if (quizForm) quizForm.style.display = 'none';
    if (quizSidebar) quizSidebar.style.display = 'none';

    const quizComplete = document.getElementById('quizComplete');
    if (quizComplete) quizComplete.classList.add('show');

    // Calculate results
    setTimeout(() => {
        const result = calculateResult();

        // Save quiz result to backend
        fetch('/api/save-quiz-result', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                science: Math.round(result.scores.science),
                commerce: Math.round(result.scores.commerce),
                arts: Math.round(result.scores.arts),
                vocational: Math.round(result.scores.vocational),
                stream: result.recommendedStream
            })
        }).then(response => response.json())
            .then(data => {
                // Redirect to result page
                const params = new URLSearchParams();
                params.append('stream', result.recommendedStream);
                Object.keys(result.scores).forEach(stream => {
                    params.append(stream, Math.round(result.scores[stream]));
                });
                window.location.href = `/result?${params.toString()}`;
            })
            .catch(error => {
                console.error('Error:', error);
                // Still redirect even if save fails
                const params = new URLSearchParams();
                params.append('stream', result.recommendedStream);
                Object.keys(result.scores).forEach(stream => {
                    params.append(stream, Math.round(result.scores[stream]));
                });
                window.location.href = `/result?${params.toString()}`;
            });
    }, 1500);
}

// ============ RESULT CALCULATION - COLLEGE RECOMMENDATION ============
function calculateResult() {
    // College recommendation categories
    const collegeScores = {
        engineering: 0,      // IIT/NIT/Tier-1 Engineering colleges
        science: 0,          // Science colleges with BSc/research focus
        medicine: 0,         // Medical colleges (AIIMS/Government medical)
        commerce: 0,         // Commerce/BBA colleges
        arts: 0              // Arts/Humanities colleges
    };

    // Calculate scores for each answer
    Object.keys(selectedAnswers).forEach(questionId => {
        const optionIndex = selectedAnswers[questionId];
        const question = quizData.find(q => q.id == questionId);

        if (optionIndex !== null && question && question.options[optionIndex]) {
            const scores = question.options[optionIndex].scores;
            Object.keys(scores).forEach(collegeType => {
                collegeScores[collegeType] += scores[collegeType];
            });
        }
    });

    // Normalize scores to 0-100
    const maxScore = totalQuestions * 5; // Max 5 points per question (college focused)
    Object.keys(collegeScores).forEach(collegeType => {
        collegeScores[collegeType] = Math.round((collegeScores[collegeType] / maxScore) * 100);
    });

    // Adjust scores based on user's academic performance
    if (typeof userData !== 'undefined' && userData.academicPercentage > 0) {
        const performanceMultiplier = userData.academicPercentage / 100;

        if (userData.academicPercentage >= 85) {
            // Excellent students - Boost top-tier colleges
            collegeScores.engineering = Math.round(collegeScores.engineering * 1.15);
            collegeScores.medicine = Math.round(collegeScores.medicine * 1.15);
        } else if (userData.academicPercentage >= 70) {
            // Good students - Boost higher colleges
            collegeScores.engineering = Math.round(collegeScores.engineering * 1.05);
            collegeScores.medicine = Math.round(collegeScores.medicine * 1.05);
        } else if (userData.academicPercentage >= 50) {
            // Average students - Balanced boost
            Object.keys(collegeScores).forEach(type => {
                collegeScores[type] = Math.round(collegeScores[type] * 1.02);
            });
        }
    }

    // Cap scores at 100
    Object.keys(collegeScores).forEach(collegeType => {
        collegeScores[collegeType] = Math.min(100, collegeScores[collegeType]);
    });

    // Find recommended college type
    const recommendedCollege = Object.keys(collegeScores).reduce((a, b) =>
        collegeScores[a] > collegeScores[b] ? a : b
    );

    return {
        scores: collegeScores,
        recommendedStream: recommendedCollege, // Using same field name for backend compatibility
        collegeType: recommendedCollege
    };
}
