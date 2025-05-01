Main Functions and Features:

    Displaying the Quiz:
        The program creates a window (form) with the title "Synag (Test)".
        Inside the window, questions (questions) are displayed one after another.
        Each question is accompanied by several answer options presented as radio buttons (only one option can be selected).
        Different fonts are used for titles, questions, answer options, and buttons for better visual presentation.
        
    User Interaction:
        The user reads the question and selects one of the provided answer options.
        There is a button "Netijäni görkez (Show Result)": Clicking it triggers the program to calculate the results.
        There is a button "Täzeden başla (Reset)": This resets all the user's selected answers, allowing them to take the test again.

    Calculation and Display of Results:
        The calculate_results_data function computes the number of correct answers, incorrect answers, and questions the user did not answer.
        The show_result_window function opens a new pop-up window ("Synagyň Netijesi (Test Result)") to display the results.
        The results window shows:
            Number of correct answers (in green).
            Number of incorrect answers (in red).
            Number of unanswered questions (in orange).
            Total number of questions.
            Success percentage (in bold).
        If the user tries to view the results without answering all questions, the program issues a warning and asks if they wish to proceed.
        The results window has a "Ýap (Close)" button.

    Question Management (Key Feature):
        There is a button "Soraglary Dolandyr (Manage)" (Manage Questions).
        Clicking it opens another window ("Soraglary Dolandyrmak (Manage Questions)").
        In this window, you can:
            View the list of current questions.
            Delete a selected question from the list.
            Add a new question: To do this, enter the question text, answer options (separated by commas), and the correct answer option into the respective fields.
            Input validation is included (cannot add a question with empty fields, requires at least two answer options, the correct answer must be among the options).
        Dynamic Update: After adding or deleting a question, the main quiz interface is automatically rebuilt (rebuild_quiz_ui) to display the updated list of questions.

    Interface Language: All labels on buttons, text elements, and messages are in the Turkmen language.

In Summary:

This is not just a static quiz, but a dynamic application that allows users not only to take tests but also to edit the question database (add/delete questions) directly from the program's interface. It is built using Tkinter and has a clear structure for displaying and managing questions.
