class Markdown:

    def rewrite(self):
        with open('output.md', 'w') as text_write:
            text_write.write('')

    def append_text(self):
        with open('output.md', 'a') as text_write:
            text_input = input('>')
            text_write.write(f'\n\n{text_input}')


    def new_line(self):
        with open('output.md', 'a') as text_new_line:
            text_new_line.write('\n')


    def italic_line(self):
        with open('output.md', 'a') as text_write:
            italic_text = input('>')
            text_write.write(f'\n\n*{italic_text}*')


    def bold_line(self):
        with open('output.md', 'a') as text_write:
            bold_text = input('>')
            text_write.write(f'\n\n**{bold_text}**')


    def bold_and_italic_line(self):
        with open('output.md', 'a') as text_write:
            bold_and_italic_text = input('>')
            text_write.write(f'\n\n***{bold_and_italic_text}***')


    def header_line(self):
        print('Hello please enter level of Header in range 1 to 6')
        header_level_input = int(input('>'))
        print(header_level_input)
        if header_level_input >= 1 and header_level_input <= 6:
            print('1')
            header_level = ('#' * header_level_input)
            print(header_level)
            with open('output.md', 'a') as text_write:
                italic_text = input('>')
                print(italic_text)
                text_write.write(f'\n{header_level} {italic_text}\n')


        else:
            print("Out of range")
            Markdown.header_line(Markdown)

    def link_line(self):
        with open('output.md', 'a') as text_write:
            link_name = input('Link name:>')
            link = input('link:>')
            text_write.write(f'\n\n[{link_name}]({link})')


    def code_line(self):
        with open('output.md', 'a') as text_write:
            code_text = input('>')
            text_write.write(f"\n`{code_text}`")


    def oredered_list_line(self):
        print("input numbers of lines")
        number_line_input = int(input('>'))
        x = 0

        if number_line_input <= 0:
            print("error\nPlease enter number bigger then 0")
            Markdown.oredered_list_line(Markdown)

        else:
            while x < number_line_input:
                x = x + 1
                if x <= number_line_input:
                    with open('output.md', 'a') as text_write:
                        ordered_list_text = input('>')
                        text_write.write(f'\n1. {ordered_list_text}')

            else:
                Markdown.menu(Markdown)

    def unordered_list_line(self):
        print("input numbers of lines")
        number_line_input = int(input('>'))
        x = 0

        if number_line_input <= 0:
            print("error\nPlease enter number bigger then 0")
            Markdown.unordered_list_line(Markdown)

        else:
            while x < number_line_input:
                x = x + 1
                if x <= number_line_input:
                    with open('output.md', 'a') as text_write:
                        unordered_list_text = input('>')
                        text_write.write(f'\n- {unordered_list_text}')

            else:
                Markdown.menu(Markdown)


    def menu(self):
        print('Rewrite? y/n')
        rewrite_input = input(">")
        if rewrite_input == ("y"):
            Markdown.rewrite(Markdown)
        else:
            pass

        print("Welcome to Markdown editor by Fedorov")
        print('Chose formatting type')
        print("1.plain - звичайний текст без форматування"
              "\n2.bold - напівжирний"
              "\n3.italic - курсив"
              "\n4.bold & italic напівжирний курсив"
              "\n5.inline-code вбудований код"
              "\n6.link - посилання"
              "\n7.header - Заголовок"
              "\n8.unordered-list - невпорядкований список"
              "\n9.ordered-list упорядкований список"
              "\n10.new-line - перехід на новий рядок"
              "\ndone - зберегти розмітку та зваершити програму")

        entering_formatter = input('Enter: >')
        if int(entering_formatter) == 1:
            Markdown.append_text(Markdown)
        elif int(entering_formatter) == 2:
            Markdown.bold_line(Markdown)
        elif int(entering_formatter) == 3:
            Markdown.italic_line(Markdown)
        elif int(entering_formatter) == 4:
            Markdown.bold_and_italic_line(Markdown)
        elif int(entering_formatter) == 5:
            Markdown.code_line(Markdown)
        elif int(entering_formatter) == 6:
            Markdown.link_line(Markdown)
        elif int(entering_formatter) == 7:
            Markdown.header_line(Markdown)
        elif int(entering_formatter) == 8:
            Markdown.unordered_list_line(Markdown)
        elif int(entering_formatter) == 9:
            Markdown.oredered_list_line(Markdown)
        elif int(entering_formatter) == 10:
            Markdown.new_line(Markdown)
        elif entering_formatter == ('done'):

            pass

while True:
    Markdown.menu(Markdown)
