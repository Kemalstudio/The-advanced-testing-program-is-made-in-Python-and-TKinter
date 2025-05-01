import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox  
from tkinter import simpledialog 

form = tk.Tk()
form.geometry("950x1000") 
form.title("Synag (Test)")

title_font = tkFont.Font(family="Arial", size=14, weight="bold")
question_font = tkFont.Font(family="Arial", size=12, weight="bold")
option_font = tkFont.Font(family="Arial", size=11)
button_font = tkFont.Font(family="Arial", size=12, weight="bold")
result_title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
result_text_font = tkFont.Font(family="Helvetica", size=12)
result_percent_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
manage_button_font = tkFont.Font(family="Arial", size=10)

questions = [
    ("Python name?", ["Programmirlemek dili",
     "Oyun yasalyan dili", "Ikisem dal"], "Programmirlemek dili"),
    ("HTML näme üçin ulanylýar?", [
     "Programmirlemek", "Web sahypalary dizaýn etmek", "Grafika döretmek"], "Web sahypalary dizaýn etmek"),
    ("Python-da maglumatlar tipi haýsy?", ["int", "span", "bold"], "int"),
    ("CSS näme üçin ulanylýar?", ["Dizaýn", "Serwer", "Maýyplamak"], "Dizaýn"),
    ("JavaScript näme üçin ulanylýar?", [
     "Interaktiwlik üçin", "Sazlamak üçin", "Saklamak üçin"], "Interaktiwlik üçin"),
    ("Python-da funksiyani nädip döretmeli?",
     ["function myFunc()", "def myFunc():", "fun myFunc[]"], "def myFunc():")
]

vars_list = []
question_widgets = [] 

quiz_frame = tk.Frame(form, padx=10, pady=10)
quiz_frame.pack(fill="both", expand=True)

control_button_frame = tk.Frame(form)
control_button_frame.pack(pady=10)

def calculate_results_data():
    correct = 0
    total = len(questions)
    unanswered = 0
    if not questions: 
        return 0, 0, 0, 0, 0

    for idx, (_, _, correct_ans) in enumerate(questions):
        if idx < len(vars_list):
            selected_option = vars_list[idx].get()
            if not selected_option:
                unanswered +=1
            elif selected_option == correct_ans:
                correct += 1
        else:
             print(f"Warning: Mismatch between questions and vars_list at index {idx}")
             total -= 1 

    mistakes = total - correct - unanswered
    percent = 0
    if total > 0:
        percent = round((correct / total) * 100)
    return correct, mistakes, unanswered, total, percent

def show_result_window():
    if not questions:
        messagebox.showinfo("Netije Ýok", "Görkezmek üçin hiç hili sorag ýok.")
        return

    correct, mistakes, unanswered, total, percent = calculate_results_data()

    if unanswered > 0:
       response = messagebox.askyesno("Jogaplanmadyk Soraglar",
                             f"{unanswered} sany soraga jogap bermediňiz.\n"
                             "Şonda-da netijeleri görmek isleýärsiňizmi?")
       if not response:
           return 

    result_win = tk.Toplevel(form)
    result_win.title("Synagyň Netijesi (Test Result)")
    result_win.geometry("400x350") 
    result_win.resizable(False, False)
    result_win.grab_set()

    form_x = form.winfo_x()
    form_y = form.winfo_y()
    form_w = form.winfo_width()
    form_h = form.winfo_height()
    win_w = 400
    win_h = 350
    pos_x = form_x + (form_w // 2) - (win_w // 2)
    pos_y = form_y + (form_h // 2) - (win_h // 2)
    result_win.geometry(f"+{pos_x}+{pos_y}")

    result_frame = tk.Frame(result_win, padx=20, pady=20, relief=tk.RIDGE, borderwidth=5, bg="#f0f0f0")
    result_frame.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Label(result_frame, text="Netijeler", font=result_title_font, bg="#f0f0f0").pack(pady=(0, 15))

    tk.Label(result_frame, text=f"Dogry jogaplar: {correct}", font=result_text_font, fg="green", bg="#f0f0f0").pack(anchor="w", pady=2)
    tk.Label(result_frame, text=f"Nädogry jogaplar: {mistakes}", font=result_text_font, fg="red", bg="#f0f0f0").pack(anchor="w", pady=2)
    tk.Label(result_frame, text=f"Jogaplanmadyk: {unanswered}", font=result_text_font, fg="orange", bg="#f0f0f0").pack(anchor="w", pady=2)
    tk.Label(result_frame, text=f"Jemi soraglar: {total}", font=result_text_font, bg="#f0f0f0").pack(anchor="w", pady=2)

    tk.Label(result_frame, text=f"Üstünlik: {percent}%", font=result_percent_font, fg="#0052cc", bg="#f0f0f0").pack(pady=(15, 10))

    close_button = tk.Button(
        result_frame, text="Ýap (Close)", command=result_win.destroy,
        font=button_font, bg="#e74c3c", fg="white", padx=10
    )
    close_button.pack(pady=(10, 0))
    result_win.wait_window()

def reset_quiz():
    for var in vars_list:
        var.set("") 

def rebuild_quiz_ui():
    global vars_list, question_widgets

    for widget in question_widgets:
        widget.destroy()

    vars_list.clear()
    question_widgets.clear()

    for i, (question, options, _) in enumerate(questions):
        q_label = tk.Label(quiz_frame, text=f"{i+1}) {question}", font=question_font)
        q_label.pack(anchor="w", padx=10, pady=(15, 5))
        question_widgets.append(q_label) 

        var = tk.StringVar()
        var.set("") 
        vars_list.append(var) 

        options_frame = tk.Frame(quiz_frame)
        options_frame.pack(anchor="w", padx=30)
        question_widgets.append(options_frame) 

        for option in options:
            rb = tk.Radiobutton(
                options_frame, text=option, variable=var, value=option,
                font=option_font, anchor="w"
            )
            rb.pack(anchor="w")

    reset_quiz()

def open_manage_window():
    manage_win = tk.Toplevel(form)
    manage_win.title("Soraglary Dolandyrmak (Manage Questions)")
    manage_win.geometry("550x500")
    manage_win.resizable(True, True) 
    manage_win.grab_set()

    list_frame = tk.Frame(manage_win, bd=2, relief=tk.GROOVE)
    list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    add_frame = tk.Frame(manage_win, bd=2, relief=tk.GROOVE)
    add_frame.pack(pady=10, padx=10, fill=tk.X)

    tk.Label(list_frame, text="Bar bolan Soraglar:", font=question_font).pack(anchor="nw")
    listbox_frame = tk.Frame(list_frame) 
    listbox_frame.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
    question_listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, font=option_font, height=10)
    scrollbar.config(command=question_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    question_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def refresh_listbox():
        question_listbox.delete(0, tk.END) 
        for i, (q_text, _, _) in enumerate(questions):
            display_text = f"{i+1}. {q_text[:50]}{'...' if len(q_text)>50 else ''}"
            question_listbox.insert(tk.END, display_text)

    refresh_listbox() 

    def delete_selected_question():
        selected_indices = question_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Saýlanmady", "Pozmak üçin sorag saýlaň.", parent=manage_win)
            return

        selected_index = selected_indices[0] 

        q_text = questions[selected_index][0][:30] 
        if not messagebox.askyesno("Tassyklaň", f"'{q_text}...' soragyny pozmak isleýärsiňizmi?", parent=manage_win):
            return
        del questions[selected_index]

        refresh_listbox()
        rebuild_quiz_ui() 
        messagebox.showinfo("Üstünlikli", "Sorag pozuldy.", parent=manage_win)

    delete_button = tk.Button(list_frame, text="Saýlanan soragy poz (Delete Selected)", command=delete_selected_question, font=manage_button_font, bg="#e74c3c", fg="white")
    delete_button.pack(pady=5)

    tk.Label(add_frame, text="Täze Sorag Goşmak:", font=question_font).grid(row=0, column=0, columnspan=3, sticky="w", pady=5)

    tk.Label(add_frame, text="Sorag Teksti:", font=option_font).grid(row=1, column=0, sticky="w")
    new_q_text_entry = tk.Entry(add_frame, width=50, font=option_font)
    new_q_text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=2, sticky="we")

    tk.Label(add_frame, text="Variantlar (otyr bilen bölüň):", font=option_font).grid(row=2, column=0, sticky="w")
    new_options_entry = tk.Entry(add_frame, width=50, font=option_font)
    new_options_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=2, sticky="we")
    new_options_entry.insert(0, "Variant1, Variant2, Variant3") 

    tk.Label(add_frame, text="Dogry Jogap:", font=option_font).grid(row=3, column=0, sticky="w")
    new_correct_ans_entry = tk.Entry(add_frame, width=50, font=option_font)
    new_correct_ans_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=2, sticky="we")
    new_correct_ans_entry.insert(0, "Variant1") 

    def add_new_question():
        q_text = new_q_text_entry.get().strip()
        options_str = new_options_entry.get().strip()
        correct_ans = new_correct_ans_entry.get().strip()

        if not q_text or not options_str or not correct_ans:
            messagebox.showerror("Boş Meýdanlar", "Ähli meýdanlary dolduryň.", parent=manage_win)
            return

        options = [opt.strip() for opt in options_str.split(',') if opt.strip()] 

        if not options or len(options) < 2:
             messagebox.showerror("Ýalňyş Variantlar", "Iň azyndan iki sany dogry variant giriziň, otyr bilen bölünen.", parent=manage_win)
             return

        if correct_ans not in options:
            messagebox.showerror("Dogry Jogap Ýalňyş", f"'{correct_ans}' dogry jogaby görkezilen variantlaryň arasynda bolmaly.", parent=manage_win)
            return

        questions.append((q_text, options, correct_ans))
        refresh_listbox()
        rebuild_quiz_ui() 

        new_q_text_entry.delete(0, tk.END)
        new_options_entry.delete(0, tk.END)
        new_correct_ans_entry.delete(0, tk.END)
        new_options_entry.insert(0, "Variant1, Variant2, Variant3") 
        new_correct_ans_entry.insert(0, "Variant1") 

        messagebox.showinfo("Üstünlikli", "Täze sorag goşuldy.", parent=manage_win)

    add_button = tk.Button(add_frame, text="Soragy Goş (Add Question)", command=add_new_question, font=manage_button_font, bg="#4CAF50", fg="white")
    add_button.grid(row=4, column=1, pady=10, padx=5, sticky="e")

    close_manage_button = tk.Button(add_frame, text="Ýap (Close)", command=manage_win.destroy, font=manage_button_font)
    close_manage_button.grid(row=4, column=2, pady=10, padx=5, sticky="w")

    add_frame.columnconfigure(1, weight=1)

    manage_win.wait_window()
    
submit_button = tk.Button(
    control_button_frame, text="Netijäni görkez (Show Result)", command=show_result_window,
    font=button_font, bg="#4CAF50", fg="white", padx=10, pady=5
)
submit_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(
    control_button_frame, text="Täzeden başla (Reset)", command=reset_quiz,
    font=button_font, bg="#f39c12", fg="white", padx=10, pady=5
)
reset_button.pack(side=tk.LEFT, padx=5)

manage_button = tk.Button(
    control_button_frame, text="Soraglary Dolandyr (Manage)", command=open_manage_window, 
    font=button_font, bg="#3498db", fg="white", padx=10, pady=5 
)
manage_button.pack(side=tk.LEFT, padx=5)

rebuild_quiz_ui()

form.mainloop()