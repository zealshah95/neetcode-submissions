class TextProcessor:
    # # Implement method overloading for format_text method
    # def format_text(self, arg1: str, arg2: str=None) -> str:
    #     if arg2 == None:
    #         return arg1.upper()
    #     else:
    #         return arg1 + arg2

    # Solution 2:
    def format_text(self, *args:str):
        output = ""
        if len(args) == 1:
            return args[0].upper()
        else:
            for arg in args:
                output += arg
            return output



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
