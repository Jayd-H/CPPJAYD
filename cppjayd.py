import os
import argparse
import json
import subprocess

def create_project(project_name, bits):
    project_dir = os.path.join(os.getcwd(), project_name)
    vscode_dir = os.path.join(project_dir, '.vscode')
    main_cpp = os.path.join(project_dir, 'main.cpp')

    os.makedirs(vscode_dir, exist_ok=True)

    with open(main_cpp, 'w') as file:
        file.write('#include <iostream>\n\nint main() {\n    std::cout << "Hello, World!" << std::endl;\n    return 0;\n}')

    tasks_path = os.path.join(vscode_dir, 'tasks.json')
    launch_path = os.path.join(vscode_dir, 'launch.json')

    tasks_content = {
    }

    launch_content = {
    }

    with open(tasks_path, 'w') as file:
        json.dump(tasks_content, file, indent=4)

    with open(launch_path, 'w') as file:
        json.dump(launch_content, file, indent=4)

    subprocess.run(['code', project_dir])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set up a new C++ project for VS Code.')
    parser.add_argument('bits', choices=['32', '64'], help='The bit version for the project (32 or 64).')
    parser.add_argument('projectname', help='The name of the project.')
    args = parser.parse_args()

    create_project(args.projectname, args.bits)
