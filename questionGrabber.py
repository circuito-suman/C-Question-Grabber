import os  # Importing the os module for directory and file operations

def extract_questions_from_code(file_path):
    """
    Extracts questions from comments in a C code file.
    
    Args:
        file_path (str): Path to the C code file.
        
    Returns:
        list: List of questions extracted from the code file.
    """
    questions = []  # List to store extracted questions
    with open(file_path, 'r') as file:  # Opening the file in read mode
        lines = file.readlines()  # Reading all lines from the file
        in_comment_block = False  # Flag to track whether inside a comment block
        current_question = ""  # Variable to store the current question being extracted
        for line in lines:  # Iterating through each line in the file
            line = line.strip()  # Removing leading and trailing whitespaces from the line
            if line.startswith("/*"):  # Checking if the line starts a comment block
                in_comment_block = True  # Setting the flag to indicate inside a comment block
            if in_comment_block:  # If inside a comment block
                if line.endswith("*/"):  # If the line ends the comment block
                    in_comment_block = False  # Setting the flag to indicate outside a comment block
                else:
                    if line.startswith("*"):  # If the line is a continuation of a multi-line comment
                        current_question += line[1:].strip() + "\n"  # Appending the comment (excluding '*') to the current question
                    else:
                        current_question += line.strip() + "\n"  # Appending the line to the current question
            elif line.startswith("//"):  # If the line is a single-line comment
                questions.append(line[2:].strip())  # Appending the comment (excluding '//') to the list of questions
            elif line.startswith("/*"):  # If the line starts a new comment block
                current_question += line[2:].strip() + "\n"  # Appending the comment (excluding '/*') to the current question
            elif line.endswith("*/"):  # If the line ends a comment block
                current_question += line[:-2].strip() + "\n"  # Appending the comment (excluding '*/') to the current question
                questions.append(current_question.strip())  # Appending the completed question to the list of questions
                current_question = ""  # Resetting the current question variable
    return questions  # Returning the list of extracted questions

def main():
    directory = "C:/Users/KIIT0001/OneDrive/Documents/ccodes"  # Path to your directory containing C code files
    lab_files = os.listdir(directory)  # Getting the list of files in the directory
    for file_name in lab_files:  # Iterating through each file in the directory
        if file_name.endswith(".c"):  # Checking if the file is a C code file
            file_path = os.path.join(directory, file_name)  # Creating the full file path
            questions = extract_questions_from_code(file_path)  # Extracting questions from the code file
            print(f"Questions extracted from {file_name}:")  # Printing the file name
            for question in questions:  # Iterating through each extracted question
                print(question)  # Printing the extracted question
            print("="*50)  # Printing a separator line

if __name__ == "__main__":  # Checking if the script is run directly
    main()  # Calling the main function
