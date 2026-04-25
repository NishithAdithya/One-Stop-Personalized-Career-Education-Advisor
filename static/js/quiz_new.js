// ============ QUIZ DATA (COMPREHENSIVE 12 QUESTIONS) ============

const quizData = [
    {
        id: 1,
        question: "What do you enjoy doing most in your free time?",
        options: [
            { text: "Solving math problems and coding", scores: { science: 4, commerce: 1, arts: 0, vocational: 1 } },
            { text: "Reading books and analyzing stories", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "Managing finances and planning budgets", scores: { science: 1, commerce: 4, arts: 1, vocational: 0 } },
            { text: "Building things and fixing mechanical objects", scores: { science: 2, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 2,
        question: "Which subject comes easiest to you?",
        options: [
            { text: "Physics and Mathematics", scores: { science: 4, commerce: 1, arts: 0, vocational: 2 } },
            { text: "History and Literature", scores: { science: 0, commerce: 0, arts: 4, vocational: 0 } },
            { text: "Economics and Business Studies", scores: { science: 1, commerce: 4, arts: 1, vocational: 0 } },
            { text: "Practical/Hands-on learning", scores: { science: 1, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 3,
        question: "Your career goal is to become:",
        options: [
            { text: "Engineer, Doctor, or Scientist", scores: { science: 4, commerce: 0, arts: 0, vocational: 1 } },
            { text: "Lawyer, Journalist, or IAS Officer", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "Businessman, Accountant, or Banker", scores: { science: 1, commerce: 4, arts: 1, vocational: 0 } },
            { text: "Skilled Technician or Tradesperson", scores: { science: 1, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 4,
        question: "How do you prefer to learn?",
        options: [
            { text: "Through experiments, labs, and theory", scores: { science: 4, commerce: 1, arts: 0, vocational: 2 } },
            { text: "Through reading, discussions, and debates", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "Through case studies and real-world examples", scores: { science: 1, commerce: 4, arts: 2, vocational: 1 } },
            { text: "Through hands-on projects and practical work", scores: { science: 1, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 5,
        question: "What matters most to you in a job?",
        options: [
            { text: "Innovation and research opportunities", scores: { science: 4, commerce: 0, arts: 1, vocational: 1 } },
            { text: "Making social impact and helping people", scores: { science: 1, commerce: 1, arts: 4, vocational: 2 } },
            { text: "Financial growth and business success", scores: { science: 0, commerce: 4, arts: 0, vocational: 1 } },
            { text: "Stable income and job security", scores: { science: 1, commerce: 2, arts: 1, vocational: 4 } }
        ]
    },
    {
        id: 6,
        question: "How would you describe your analytical skills?",
        options: [
            { text: "Excellent with numbers and logic", scores: { science: 4, commerce: 4, arts: 1, vocational: 1 } },
            { text: "Good at understanding people and ideas", scores: { science: 0, commerce: 1, arts: 4, vocational: 1 } },
            { text: "Average - prefer practical application", scores: { science: 1, commerce: 1, arts: 1, vocational: 4 } },
            { text: "Strong problem-solving abilities", scores: { science: 4, commerce: 2, arts: 1, vocational: 3 } }
        ]
    },
    {
        id: 7,
        question: "Which statement describes you best?",
        options: [
            { text: "I love discovering 'how things work'", scores: { science: 4, commerce: 0, arts: 1, vocational: 3 } },
            { text: "I enjoy writing and creative expression", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "I'm interested in business and entrepreneurship", scores: { science: 1, commerce: 4, arts: 1, vocational: 1 } },
            { text: "I prefer practical, immediate results", scores: { science: 1, commerce: 1, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 8,
        question: "Your approach to a problem is to:",
        options: [
            { text: "Analyze data and use scientific method", scores: { science: 4, commerce: 2, arts: 0, vocational: 1 } },
            { text: "Research and study different perspectives", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "Apply business logic and financial analysis", scores: { science: 1, commerce: 4, arts: 1, vocational: 0 } },
            { text: "Find practical hands-on solutions", scores: { science: 1, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 9,
        question: "What's your ideal work environment?",
        options: [
            { text: "Laboratory, research center, or tech company", scores: { science: 4, commerce: 0, arts: 0, vocational: 1 } },
            { text: "Media, publishing, or government office", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "Corporate office or trading floor", scores: { science: 0, commerce: 4, arts: 1, vocational: 0 } },
            { text: "Workshop, factory, or field work", scores: { science: 1, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 10,
        question: "How important is continued education to you?",
        options: [
            { text: "Very important - love learning forever", scores: { science: 4, commerce: 2, arts: 4, vocational: 1 } },
            { text: "Important - want specialized skills", scores: { science: 2, commerce: 3, arts: 2, vocational: 3 } },
            { text: "Moderate - practical experience matters", scores: { science: 1, commerce: 2, arts: 1, vocational: 2 } },
            { text: "Less important - learn on the job", scores: { science: 0, commerce: 1, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 11,
        question: "Which achievement would satisfy you most?",
        options: [
            { text: "Inventing something or making a scientific discovery", scores: { science: 4, commerce: 0, arts: 1, vocational: 2 } },
            { text: "Writing a book or creating impactful content", scores: { science: 0, commerce: 0, arts: 4, vocational: 0 } },
            { text: "Building a successful business empire", scores: { science: 0, commerce: 4, arts: 1, vocational: 1 } },
            { text: "Mastering a skilled trade perfectly", scores: { science: 1, commerce: 0, arts: 0, vocational: 4 } }
        ]
    },
    {
        id: 12,
        question: "What's your current academic strength?",
        options: [
            { text: "Science & Maths are my strong subjects", scores: { science: 4, commerce: 1, arts: 0, vocational: 2 } },
            { text: "Language & Social Studies are my best", scores: { science: 0, commerce: 1, arts: 4, vocational: 0 } },
            { text: "Good at Math and business subjects", scores: { science: 2, commerce: 4, arts: 0, vocational: 1 } },
            { text: "All subjects equally or prefer practical work", scores: { science: 1, commerce: 1, arts: 1, vocational: 4 } }
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

    let optionsHTML = `<h2>${question.question}</h2><div class="options-group">`;

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

// ============ RESULT CALCULATION ============
function calculateResult() {
    const streamScores = {
        science: 0,
        commerce: 0,
        arts: 0,
        vocational: 0
    };

    // Calculate scores for each answer
    Object.keys(selectedAnswers).forEach(questionId => {
        const optionIndex = selectedAnswers[questionId];
        const question = quizData.find(q => q.id == questionId);

        if (optionIndex !== null && question && question.options[optionIndex]) {
            const scores = question.options[optionIndex].scores;
            Object.keys(scores).forEach(stream => {
                streamScores[stream] += scores[stream];
            });
        }
    });

    // Normalize scores to 0-100
    const maxScore = totalQuestions * 4; // Max 4 points per question
    Object.keys(streamScores).forEach(stream => {
        streamScores[stream] = Math.round((streamScores[stream] / maxScore) * 100);
    });

    // Find recommended stream
    const recommendedStream = Object.keys(streamScores).reduce((a, b) =>
        streamScores[a] > streamScores[b] ? a : b
    );

    return {
        scores: streamScores,
        recommendedStream: recommendedStream
    };
}
