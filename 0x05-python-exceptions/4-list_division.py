#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        res = []
        for rec in range(list_length):
                div = 0
                try:
                        div = my_list_1[rec]/my_list_2[rec]
                except (TypeError):
                        print("wrong type")
                        div = 0
                except (ZeroDivisionError):
                        print("division by 0")
                        div = 0
                except (IndexError):
                        print("out of range")
                        div = 0
                finally:
                        res.append(div)
        return (res)
