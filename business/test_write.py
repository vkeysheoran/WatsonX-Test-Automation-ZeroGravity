import os

class TestWrite():
    def write_file(content, task_title, story_id):
        file_name = task_title.lower()
        file_name = "_".join(file_name.split())
        file_name = f"test_{file_name}.py"
        directory = f'automation_tests/{story_id}'
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        
        return file_path