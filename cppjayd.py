import os
import argparse
import shutil
import subprocess
import json


def create_project(project_name, bits, open_vscode):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    project_dir = os.path.join(os.getcwd(), project_name)
    vscode_dir = os.path.join(project_dir, ".vscode")
    templates_dir = current_dir

    os.makedirs(vscode_dir, exist_ok=True)

    # Create main.cpp
    main_cpp_path = os.path.join(project_dir, "main.cpp")
    with open(main_cpp_path, "w") as main_cpp_file:
        main_cpp_file.write(
            '#include <iostream>\n\nint main() {\n    std::cout << "Hello, World!" << std::endl;\n    return 0;\n}'
        )

    # Copy tasks.json and launch.json templates
    tasks_template_path = os.path.join(templates_dir, "tasks.json")
    launch_template_path = os.path.join(templates_dir, "launch.json")

    shutil.copy(tasks_template_path, vscode_dir)
    shutil.copy(launch_template_path, vscode_dir)

    # Modify tasks.json if necessary based on the bits argument
    tasks_json_path = os.path.join(vscode_dir, "tasks.json")
    with open(tasks_json_path, "r+") as tasks_file:
        tasks_content = json.load(tasks_file)
        tasks_file.seek(0)
        json.dump(tasks_content, tasks_file, indent=4)
        tasks_file.truncate()

    # Conditionally launch VS Code with the new project directory
    if open_vscode:
        subprocess.run(["code", project_dir])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Set up a new C++ project for VS Code."
    )
    parser.add_argument(
        "bits", choices=["32", "64"], help="The bit version for the project (32 or 64)."
    )
    parser.add_argument("projectname", help="The name of the project.")
    parser.add_argument(
        "--vs", help="Open the project in Visual Studio Code.", action="store_true"
    )
    args = parser.parse_args()

    create_project(args.projectname, args.bits, args.vs)
