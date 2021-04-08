class Pen_drive:

    def store_data(self):
        print(self, "is storing data")

    def store_movie(self, movie_name, size):
        print(self, 'is storing', movie_name, 'with size', size)

    def delete_movie(self, movie_name):
        print(movie_name, "is deleted from", self)


d1 = Pen_drive()
d2 = Pen_drive()
d3 = Pen_drive()

d2.store_data()
d1.store_movie('Avengers', 50)
d1.store_movie("KGF", 20)
d2.delete_movie('Alien')
d3.store_movie('Babhubali', 400)
d2.delete_movie('49204C6F766520596F75 😀')  # Identify the meaning of 49204C6F766520596F75
