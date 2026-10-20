from pyscript import display, document

def add_brand(e):
    document.getElementById("output1").innerHTML = ""
    
    brands = ('Uniqlo', 'Bench', 'Zara')

input_brand = document.getElementById("input1").value

