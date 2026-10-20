from pyscript import display, document

def add_brand(e):
    document.getElementById("output1").innerHTML = ""
    #1
    brands = {'Uniqlo', 'Bench', 'Zara'}
    #2
    input_brand = document.getElementById("input1").value

    #assign the value to set variables
    new_brand_set ={input_brand}  

    #3
    all_brands = brands | new_brand_set
    #4
    total_brands = len(brands | new_brand_set)

    #display the items in ascending order (A-Z) seperated by br
    brand_list = "<br>".join(sorted(all_brands))

    #display
    document.getElementById("output1").innerHTML = f'All Brands: <br> {brand_list}'
    display(f'Total Brands: {total_brands}', target = "output1")
