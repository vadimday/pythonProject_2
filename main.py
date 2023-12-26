def main():
   print("Начало Конец")

   start = int(input("Начало: "))

   end = int(input("Конец: "))

   print("Все:")

   for i in range(start, end + 1):

       print(i, end=" ")

   print()

   print("Упад:")

   for i in range(end, start - 1, -1):

       print(i, end=" ")

   print()

   print("Кратные 7:")

   for i in range(start, end + 1):

       if i % 7 == 0:

           print(i, end=" ")

   print()

   print("Кратные 5:")

   count = 0

   for i in range(start, end + 1):

       if i % 5 == 0:

           count += 1

   print(count)

if __name__ == "__main__":

   main()