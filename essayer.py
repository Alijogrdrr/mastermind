import tkinter as tk

def create_interface():
    # Dimensions principales
    window_width = 800
    rect_height = 30      # Hauteur de chaque rectangle
    spacing = 5           # Espacement entre les rectangles
    canvas_height = (rect_height + spacing) * 11 + spacing
    rect_width = int(0.8 * window_width)  # Chaque rectangle occupe 80% de la largeur

    # Dimensions de la zone de feedback (pour afficher 4 petits cercles)
    feedback_width = 50
    feedback_circle_radius = 5

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Jeu de Mastermind")

    # Conteneur pour le canvas et le panneau latéral (boutons)
    container = tk.Frame(root)
    container.pack()

    total_width = window_width + feedback_width + 20  # On ajoute de la place pour la zone de feedback
    drawing_canvas = tk.Canvas(container, width=total_width, height=canvas_height, bg="white")
    drawing_canvas.pack(side="left", padx=10, pady=10)

    # Listes pour stocker les IDs et coordonnées
    circles = []           # 4 cercles par ligne (saisie)
    rectangles_coords = [] # Coordonnées de chaque rectangle, utilisées pour la zone de feedback

    # Liste pour suivre les couleurs saisies pour chaque ligne (11 lignes)
    line_colors = [[] for _ in range(11)]

    # Dessin des 11 rectangles et des 4 cercles dans chacun
    for i in range(11):
        x1 = 10  # Marge à gauche
        y1 = spacing + i * (rect_height + spacing)
        x2 = x1 + rect_width
        y2 = y1 + rect_height

        drawing_canvas.create_rectangle(x1, y1, x2, y2, outline="black")
        rectangles_coords.append((x1, y1, x2, y2))

        r = 7
        gap = rect_width / 5
        for j in range(4):
            cx = x1 + gap * (j + 1)
            cy = y1 + rect_height / 2
            circle_id = drawing_canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="blue")
            circles.append(circle_id)

    current_circle = 0
    allowed_line = 0

    def change_next_circle_color(color):
        nonlocal current_circle, allowed_line
        next_row = current_circle // 4
        if next_row > allowed_line:
            print("Veuillez vérifier la ligne en cours avant de passer à la suivante.")
            return
        drawing_canvas.itemconfig(circles[current_circle], fill=color)
        line_colors[next_row].append(color)
        current_circle += 1

    def compare_line(line_index):
        secret = line_colors[0]
        guess = line_colors[line_index]
        feedback = []
        for j in range(4):
            if guess[j] == secret[j]:
                feedback.append("red")
            elif guess[j] in secret:
                feedback.append("blue")
            else:
                feedback.append("white")
        x1, y1, x2, y2 = rectangles_coords[line_index]
        margin = 5
        fb_x_start = x2 + margin
        spacing_fb = feedback_width / 5
        for k in range(4):
            cx = fb_x_start + spacing_fb * (k + 1)
            cy = y1 + rect_height / 2
            drawing_canvas.create_oval(cx - feedback_circle_radius, cy - feedback_circle_radius,
                                       cx + feedback_circle_radius, cy + feedback_circle_radius,
                                       fill=feedback[k], outline="black")
        return feedback

    def show_winning_screen():
        win_popup = tk.Toplevel(root)
        win_popup.title("Gagné !")
        label = tk.Label(win_popup, text="Vous avez gagné", font=("Helvetica", 24), fg="green")
        label.pack(padx=20, pady=20)
        def restart():
            root.destroy()
            create_interface()
        restart_button = tk.Button(win_popup, text="Recommencer", command=restart)
        restart_button.pack(pady=10)

    def verify_line():
        nonlocal allowed_line, current_circle
        if current_circle % 4 != 0 or current_circle == 0:
            print("La ligne en cours n'est pas complète.")
            return

        if allowed_line == 0:
            x1, y1, x2, y2 = rectangles_coords[0]
            drawing_canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")
            for idx in range(0, 4):
                drawing_canvas.itemconfig(circles[idx], state="hidden")
            print("Code secret vérifié et masqué.")
        else:
            feedback = compare_line(allowed_line)
            print(f"Ligne {allowed_line} vérifiée.")
            if all(fb == "red" for fb in feedback):
                show_winning_screen()
                return

        if allowed_line < 10:
            allowed_line += 1
        else:
            print("Toutes les lignes ont été vérifiées.")

    def show_line_colors():
        popup = tk.Toplevel(root)
        popup.title("Couleurs par ligne")
        text = ""
        for i, colors in enumerate(line_colors):
            text += f"Ligne {i+1}: {colors}\n"
        label = tk.Label(popup, text=text, justify="left")
        label.pack(padx=10, pady=10)

    button_frame = tk.Frame(container)
    button_frame.pack(side="right", fill="y", padx=10, pady=10)

    couleurs = ["red", "green", "blue", "yellow", "purple", "orange"]
    for col in couleurs:
        btn = tk.Button(button_frame, text=col.capitalize(), bg=col, width=10,
                        command=lambda c=col: change_next_circle_color(c))
        btn.pack(pady=5)

    verify_btn = tk.Button(button_frame, text="Vérifier", width=10, command=verify_line)
    verify_btn.pack(pady=5)

    show_btn = tk.Button(button_frame, text="Afficher les couleurs", width=15, command=show_line_colors)
    show_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_interface()
