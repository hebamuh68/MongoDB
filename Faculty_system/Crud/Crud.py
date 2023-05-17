from pymongo import MongoClient


class Crud:

    def __init__(self):
        MONGODB_URL = "mongodb+srv://heba:heba333@test.fsjvnow.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(MONGODB_URL)
        self.db = self.client.Faculty
        self.Students_collection = self.db.Students

    def Insert_student(self, name, grade, GPA):
        new_student = {
            "Name": name,
            "Grade": grade,
            "GPA": GPA
        }
        inserted_done = self.Students_collection.insert_one(new_student)
        if inserted_done:
            return "Student added successfully"

    def Search_student(self, name, grade):
        document_to_find = {"Name": name, "Grade": grade}
        self.result = self.Students_collection.find(document_to_find)
        return self.result
