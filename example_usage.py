from client import PedagogicalLessonPlanCurriculumSynthesizerClient

def main():
    client = PedagogicalLessonPlanCurriculumSynthesizerClient()
    res = client.synthesize_lesson_plan('CRISPR Cas9 Gene Editing Mechanisms', 'HIGH_SCHOOL_AP_BIOLOGY', 60)
    print('Lesson Plan Synthesizer: ' + res['curriculum_id'] + ' (' + res['subject'] + ')')
    print('Grade: ' + res['grade_level'] + ' | Bloom Level: ' + res['bloom_taxonomy_level'])
    print('Objectives: ' + str(res['learning_objectives_count']) + ' | Lab Exercises: ' + str(res['interactive_lab_exercises_count']))
    print('Curriculum URL: ' + res['curriculum_export_markdown_url'])

if __name__ == '__main__':
    main()
