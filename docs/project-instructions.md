# Project Instructions

## WEDNESDAY: Complete Workflow Phase 1

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs
2. Phase 2. **Change Authorship** - update the project to your name and GitHub account
3. Phase 3. **Read & Understand** - review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 2-4

Again, follow the instructions above to complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

## Phase 4 Suggestions

Make a small technical change that does not break the pipeline.
Choose any one of these (or a different modification as you like):

- Change how many top tokens are displayed (e.g., change `head(5)` to `head(7)`)
- Change the context window size and observe how the nearby words change:
  - Example: set `WINDOW_SIZE = 3`
- Add a new sentence to an existing category and rerun the analysis
- Add a new category with 2-3 simple sentences (follow the same pattern)
- Modify the visualization (plot a **different category** and update the title accordingly)

Confirm the script still runs successfully after your change.

## Phase 5 Suggestions

### Phase 5 Suggestion 1. New Corpus, New Categories (Directed)

Apply the same process to a new corpus.
Replace the existing corpus with one of the examples below and rerun the script.

```python
corpus = [
    # Food
    {"category": "food", "text": "The chef cooks a meal."},
    {"category": "food", "text": "The recipe uses fresh ingredients."},
    {"category": "food", "text": "The dish is served hot."},

    # Sports
    {"category": "sports", "text": "The player scored a goal."},
    {"category": "sports", "text": "The team won the game."},
    {"category": "sports", "text": "The coach leads the team."},

    # Technology
    {"category": "technology", "text": "The computer runs software."},
    {"category": "technology", "text": "The system processes data."},
    {"category": "technology", "text": "The network connects devices."}
]
```

```python
corpus = [
    # Patients
    {"category": "patient", "text": "The patient reports mild pain."},
    {"category": "patient", "text": "The patient rests after treatment."},
    {"category": "patient", "text": "The patient follows the care plan."},

    # Doctors
    {"category": "doctor", "text": "The doctor examines the patient."},
    {"category": "doctor", "text": "The doctor prescribes medication."},
    {"category": "doctor", "text": "The doctor reviews the results."},

    # Hospitals
    {"category": "hospital", "text": "The hospital admits new patients."},
    {"category": "hospital", "text": "The hospital provides emergency care."},
    {"category": "hospital", "text": "The hospital manages patient records."}
]
```

After replacing the corpus:

- Update any category references in your code if needed
- Run the full script again
- Review the output and compare patterns across the new categories
- Compare any two or more categories and describe how their token usage differs
- Explain your findings in 3-5 sentences.
- Focus on what changed and why.

Your goal is to reuse the same process on new data and interpret what changes.

### Phase 5 Suggestion 2. New Corpus, New Categories (Original Corpus)

Apply this pipeline to a new problem (choose any of these):

- Extend the corpus with new categories and analyze the results
- Replace the corpus with a new domain (e.g., animals, veterinarians, clinics)
- Create your own corpus with 2-3 categories and multiple example sentences

With your new corpus:

- Compare any two or more categories and describe how their token usage differs
- Explain your findings in 3-5 sentences.
- Focus on what changed and why.

Your goal is to reuse this process on new data and interpret the results.

## Professional Communication

Remove instructor provided content you no longer need in your project.

For example, notebook cell comments indicating the type - these are useful while learning but not usually seen in professional projects.

Make sure the title and narrative reflect your presentation.
Verify key files:

- README.md
- docs/ (source and hosted on GitHub pages)
- notebooks/ (and/or src/) reflect your project
