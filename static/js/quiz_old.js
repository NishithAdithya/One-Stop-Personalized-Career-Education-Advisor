// ============ QUIZ DATA (DYNAMIC FROM BACKEND) ============

const quizData = [
    {
        "id": 1,
        "question": "What do you enjoy doing most in your free time?",
        "options": [
            {"text": "Solving math problems and coding", "science": 4, "commerce": 1, "arts": 0, "vocational": 1},
            {"text": "Reading books and analyzing stories", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Managing finances and planning budgets", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Building things and fixing mechanical objects", "science": 2, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 2,
        "question": "Which subject comes easiest to you?",
        "options": [
            {"text": "Physics and Mathematics", "science": 4, "commerce": 1, "arts": 0, "vocational": 2},
            {"text": "History and Literature", "science": 0, "commerce": 0, "arts": 4, "vocational": 0},
            {"text": "Economics and Business Studies", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Practical/Hands-on learning", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 3,
        "question": "Your career goal is to become:",
        "options": [
            {"text": "Engineer, Doctor, or Scientist", "science": 4, "commerce": 0, "arts": 0, "vocational": 1},
            {"text": "Lawyer, Journalist, or IAS Officer", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Businessman, Accountant, or Banker", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Skilled Technician or Tradesperson", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 4,
        "question": "How do you prefer to learn?",
        "options": [
            {"text": "Through experiments, labs, and theory", "science": 4, "commerce": 1, "arts": 0, "vocational": 2},
            {"text": "Through reading, discussions, and debates", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Through case studies and real-world examples", "science": 1, "commerce": 4, "arts": 2, "vocational": 1},
            {"text": "Through hands-on projects and practical work", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 5,
        "question": "What matters most to you in a job?",
        "options": [
            {"text": "Innovation and research opportunities", "science": 4, "commerce": 0, "arts": 1, "vocational": 1},
            {"text": "Making social impact and helping people", "science": 1, "commerce": 1, "arts": 4, "vocational": 2},
            {"text": "Financial growth and business success", "science": 0, "commerce": 4, "arts": 0, "vocational": 1},
            {"text": "Stable income and job security", "science": 1, "commerce": 2, "arts": 1, "vocational": 4}
        ]
    },
    {
        "id": 6,
        "question": "How would you describe your analytical skills?",
        "options": [
            {"text": "Excellent with numbers and logic", "science": 4, "commerce": 4, "arts": 1, "vocational": 1},
            {"text": "Good at understanding people and ideas", "science": 0, "commerce": 1, "arts": 4, "vocational": 1},
            {"text": "Average - prefer practical application", "science": 1, "commerce": 1, "arts": 1, "vocational": 4},
            {"text": "Strong problem-solving abilities", "science": 4, "commerce": 2, "arts": 1, "vocational": 3}
        ]
    },
    {
        "id": 7,
        "question": "Which statement describes you best?",
        "options": [
            {"text": "I love discovering 'how things work'", "science": 4, "commerce": 0, "arts": 1, "vocational": 3},
            {"text": "I enjoy writing and creative expression", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "I'm interested in business and entrepreneurship", "science": 1, "commerce": 4, "arts": 1, "vocational": 1},
            {"text": "I prefer practical, immediate results", "science": 1, "commerce": 1, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 8,
        "question": "Your approach to a problem is to:",
        "options": [
            {"text": "Analyze data and use scientific method", "science": 4, "commerce": 2, "arts": 0, "vocational": 1},
            {"text": "Research and study different perspectives", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Apply business logic and financial analysis", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Find practical hands-on solutions", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 9,
        "question": "What's your ideal work environment?",
        "options": [
            {"text": "Laboratory, research center, or tech company", "science": 4, "commerce": 0, "arts": 0, "vocational": 1},
            {"text": "Media, publishing, or government office", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Corporate office or trading floor", "science": 0, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Workshop, factory, or field work", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 10,
        "question": "How important is continued education to you?",
        "options": [
            {"text": "Very important - love learning forever", "science": 4, "commerce": 2, "arts": 4, "vocational": 1},
            {"text": "Important - want specialized skills", "science": 2, "commerce": 3, "arts": 2, "vocational": 3},
            {"text": "Moderate - practical experience matters", "science": 1, "commerce": 2, "arts": 1, "vocational": 2},
            {"text": "Less important - learn on the job", "science": 0, "commerce": 1, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 11,
        "question": "Which achievement would satisfy you most?",
        "options": [
            {"text": "Inventing something or making a scientific discovery", "science": 4, "commerce": 0, "arts": 1, "vocational": 2},
            {"text": "Writing a book or creating impactful content", "science": 0, "commerce": 0, "arts": 4, "vocational": 0},
            {"text": "Building a successful business empire", "science": 0, "commerce": 4, "arts": 1, "vocational": 1},
            {"text": "Mastering a skilled trade perfectly", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 12,
        "question": "What's your current academic strength?",
        "options": [
            {"text": "Science & Maths are my strong subjects", "science": 4, "commerce": 1, "arts": 0, "vocational": 2},
            {"text": "Language & Social Studies are my best", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Good at Math and business subjects", "science": 2, "commerce": 4, "arts": 0, "vocational": 1},
            {"text": "All subjects equally or prefer practical work", "science": 1, "commerce": 1, "arts": 1, "vocational": 4}
        ]
    }
];

// ============ QUIZ STATE ============

let currentIndex = 0;
const answers = {};
let totalQuestions = quizData.length;
let selectedAnswers = {};
        question: "How do you feel about competitive exams (JEE, NEET, etc.)?",
        options: [
            { value: "love_competitive", label: "I love competitive challenges" },
            { value: "willing", label: "I can prepare if needed" },
            { value: "avoid_competitive", label: "I prefer to avoid highly competitive exams" }
        ]
    },
    {
        id: "q12",
        question: "What is your academic performance level?",
        options: [
            { value: "excellent", label: "Excellent (85%+ in main subjects)" },
            { value: "good", label: "Good (70-85%)" },
            { value: "average", label: "Average (50-70%)" },
            { value: "weak", label: "Below average (<50%)" }
        ]
    }
];

// ============ SCORING WEIGHTS ============

const scoreWeights = {
    q1: {
        science: { science: 3 },
        commerce: { commerce: 3 },
        arts: { arts: 3 },
        vocational: { vocational: 3 }
    },
    q2: {
        hate_math: { arts: 2, vocational: 1 },
        ok_math: { commerce: 1, science: 1 },
        love_math: { science: 3, commerce: 2 }
    },
    q3: {
        theory: { science: 2, arts: 2 },
        practical: { vocational: 3, commerce: 1 },
        mixed: { science: 1, commerce: 1, arts: 1, vocational: 1 }
    },
    q4: {
        science_subj: { science: 3 },
        business_subj: { commerce: 3 },
        language_subj: { arts: 3 },
        practical_subj: { vocational: 3 }
    },
    q5: {
        innovation: { science: 3 },
        money: { commerce: 2 },
        impact: { arts: 2 },
        stability: { commerce: 2 }
    },
    q6: {
        numbers_love: { science: 2, commerce: 2 },
        numbers_ok: { science: 1, commerce: 1 },
        numbers_avoid: { arts: 2, vocational: 1 }
    },
    q7: {
        independent: { science: 1 },
        team: { commerce: 1, arts: 1 },
        flexible: { science: 0.5, commerce: 0.5, arts: 0.5, vocational: 0.5 }
    },
    q8: {
        lab: { science: 3 },
        office: { commerce: 2, arts: 1 },
        field: { vocational: 2 },
        creative: { arts: 3 }
    },
    q9: {
        stay_local: { arts: 1, vocational: 1 },
        willing_relocate: { science: 1, commerce: 1 },
        flexible: { science: 0.5, commerce: 0.5, arts: 0.5, vocational: 0.5 }
    },
    q10: {
        higher_study: { science: 2, commerce: 1, arts: 1 },
        job: { commerce: 2, vocational: 2 },
        business: { commerce: 3 },
        skill_training: { vocational: 3 }
    },
    q11: {
        love_competitive: { science: 2 },
        willing: { science: 1, commerce: 1, arts: 1 },
        avoid_competitive: { vocational: 2, commerce: 1 }
    },
    q12: {
        excellent: { science: 2 },
        good: { science: 1, commerce: 1, arts: 1 },
        average: { commerce: 1, arts: 1, vocational: 1 },
        weak: { vocational: 2 }
    }
};

// ============ QUIZ STATE ============

let currentIndex = 0;
const answers = {};
let totalQuestions = quizData.length;

// ============ INITIALIZATION ============

document.addEventListener('DOMContentLoaded', function () {
    initializeQuiz();
});

function initializeQuiz() {
    // Initialize all answers as empty
    quizData.forEach(q => {
        answers[q.id] = null;
    });

    // Set total questions
    document.getElementById('totalQuestions').textContent = totalQuestions;

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
        const isChecked = answers[question.id] === option.value ? 'checked' : '';
        optionsHTML += `
            <label class="option-radio">
                <input 
                    type="radio" 
                    name="q${index}" 
                    value="${option.value}" 
                    ${isChecked}
                    onchange="selectOption('${question.id}', '${option.value}')"
                >
                <span class="option-label">${option.label}</span>
            </label>
        `;
    });

    optionsHTML += `</div>`;
    questionDiv.innerHTML = optionsHTML;
    container.appendChild(questionDiv);

    updateButtonStates();
}

function selectOption(questionId, value) {
    answers[questionId] = value;
    updateProgress();

    // Auto-advance after selection (optional, can remove)
    // setTimeout(() => nextQuestion(), 800);
}

function updateSidebar() {
    if (!document.querySelectorAll('.topic-item').length) return;

    document.querySelectorAll('.topic-item').forEach((item, index) => {
        if (index === currentIndex) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }

        // Mark as completed if answered
        if (answers[quizData[index].id] !== null) {
            item.classList.add('completed');
        } else {
            item.classList.remove('completed');
        }
    });
}

function updateProgress() {
    const answered = Object.values(answers).filter(a => a !== null).length;
    const progress = (answered / totalQuestions) * 100;

    document.getElementById('progressFill').style.width = progress + '%';
    document.getElementById('currentQuestion').textContent = currentIndex + 1;
    document.getElementById('questionCounter').textContent = `Question ${currentIndex + 1} of ${totalQuestions}`;
    document.getElementById('answeredCount').textContent = answered;

    // Update sidebar
    updateSidebar();
}

function updateButtonStates() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    const currentAnswer = answers[quizData[currentIndex].id];

    // Previous button
    prevBtn.disabled = currentIndex === 0;

    // Next button
    if (currentIndex === totalQuestions - 1) {
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'block';
    } else {
        nextBtn.style.display = 'block';
        submitBtn.style.display = 'none';
        nextBtn.disabled = currentAnswer === null;
    }
}

// ============ NAVIGATION ============

function nextQuestion() {
    if (currentIndex < totalQuestions - 1) {
        currentIndex++;
        renderQuestion(currentIndex);
        updateProgress();
    }
}

function previousQuestion() {
    if (currentIndex > 0) {
        currentIndex--;
        renderQuestion(currentIndex);
        updateProgress();
    }
}

// ============ QUIZ SUBMISSION ============

document.getElementById('quizForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Check if all questions are answered
    const allAnswered = Object.values(answers).every(a => a !== null);

    if (!allAnswered) {
        alert('Please answer all questions before submitting!');
        return;
    }

    submitQuiz();
});

function submitQuiz() {
    // Show loading message
    document.getElementById('quizContainer').style.display = 'none';
    document.getElementById('quizForm').style.display = 'none';
    document.getElementById('quizComplete').classList.add('show');

    // Calculate results
    setTimeout(() => {
        const result = calculateResult();

        // Redirect to result page with query parameters
        const params = new URLSearchParams();
        params.append('stream', result.recommendedStream);

        // Add individual scores
        Object.keys(result.scores).forEach(stream => {
            params.append(stream, result.scores[stream]);
        });

        window.location.href = `/result?${params.toString()}`;
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

    // Calculate scores for each answer with enhanced logic
    Object.keys(answers).forEach(questionId => {
        const answer = answers[questionId];

        if (answer && scoreWeights[questionId] && scoreWeights[questionId][answer]) {
            const weights = scoreWeights[questionId][answer];

            Object.keys(weights).forEach(stream => {
                streamScores[stream] += weights[stream];
            });
        }
    });

    // Normalize scores
    const maxScore = Math.max(...Object.values(streamScores));
    if (maxScore > 0) {
        Object.keys(streamScores).forEach(stream => {
            streamScores[stream] = Math.round((streamScores[stream] / maxScore) * 100);
        });
    }

    // Find top recommendation
    let recommendedStream = 'science';
    let maxScore2 = streamScores['science'];

    Object.keys(streamScores).forEach(stream => {
        if (streamScores[stream] > maxScore2) {
            maxScore2 = streamScores[stream];
            recommendedStream = stream;
        }
    });

    console.log('Score Results:', streamScores);
    console.log('Recommended Stream:', recommendedStream);

    return {
        recommendedStream: recommendedStream,
        scores: streamScores
    };
}