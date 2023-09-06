import customtkinter

bg_color = "#1a1a1a"
bg_color_frame = "#212121"

class LeftmenubarFrame(customtkinter.CTkFrame):
    def __init__(self, master, change_difficulty_event):
        super().__init__(master, corner_radius=0)

        self.change_difficulty_event = change_difficulty_event

        self.button_settings = customtkinter.CTkButton(
            master=self,
            width=30,
            height=30,
            text="⚙️",
            anchor="w"
        )
        self.button_settings.place(relx=0.5, rely=0.93, anchor="center")

        self._difficulty_buttons = []

        button_amauter_difficulty = customtkinter.CTkButton(
            master=self,
            width=40,
            height=30,
            text="•",
            font=("Arial", 30),
            fg_color=bg_color_frame,
            text_color="#b0d8a4",
            border_width=1,
            command=lambda: self.change_difficulty_event(0)
        )
        button_amauter_difficulty.grid(row=1, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.difficulty_buttons.append(button_amauter_difficulty)

        button_intermediate_difficulty = customtkinter.CTkButton(
            master=self,
            width=40,
            height=30,
            text="•",
            font=("Arial", 30),
            fg_color=bg_color_frame,
            text_color="#fee191",
            border_width=0,
            command=lambda: self.change_difficulty_event(1)
        )
        button_intermediate_difficulty.grid(row=2, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.difficulty_buttons.append(button_intermediate_difficulty)

        button_professional_difficulty = customtkinter.CTkButton(
            master=self,
            width=40,
            height=30,
            text="•",
            font=("Arial", 30),
            fg_color=bg_color_frame,
            text_color="#fd8060",
            border_width=0,
            command=lambda: self.change_difficulty_event(2)
        )
        button_professional_difficulty.grid(row=3, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.difficulty_buttons.append(button_professional_difficulty)

        button_nightmare_difficulty = customtkinter.CTkButton(
            master=self,
            width=40,
            height=30,
            text="•",
            font=("Arial", 30),
            fg_color=bg_color_frame,
            text_color="#e84258",
            border_width=0,
            command=lambda: self.change_difficulty_event(3)
        )
        button_nightmare_difficulty.grid(row=4, column=0, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.difficulty_buttons.append(button_nightmare_difficulty)

    @property
    def difficulty_buttons(self):
        return self._difficulty_buttons
    
    @difficulty_buttons.setter
    def spirts_buttons(self, value):
        return