# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

from datetime import datetime


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self,code: str, title: str,text: str,importance:str):

        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] = []

    def add_tag (self,tag:str):
        if tag not  in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"

    class Notebook:
        def __init__(self,notes : list):
            self.notes = []

        def add_note(self,title: str,text: str, importance: str) -> int:
            code = len(self.notes) + 1
            new_nota = Note( code, title, text, importance)
            self.notes.append(new_nota)

            return code
        def delete_note(self, code: int):
            self.notes = [note for note in self.notes if note.code != code]

        def important_notes(self) -> list[Note]:
            return [note for note in self.notes if note.importance in [Note.HIGH, Note.MEDIUM]]

        def notes_by_tag(self, tag : str)-> list[Note]:
            return [note for note in self.notes if tag in note.tags]

        def tag_with_most_notes(self) -> str:
            tag_count = {}
            for note in self.notes:
                for tag in note.tags:
                    tag_count[tag] = tag_count.get(tag, 0) + 1
            if tag_count:
                return min(tag_count,
                           key=lambda x: (-tag_count[x], x))  # Mayor cantidad, si es empate por orden alfabético
            return ""

