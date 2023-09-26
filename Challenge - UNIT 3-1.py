def linear_search_product(products: list[str], target_product_name: str):
    result_indices = []
    for i in range(len(products)):
        if products[i] == target_product_name:
            result_indices.append(i)
    return result_indices
products = ["iPhone 13", "MacBook Air", "iPad Pro", "Apple Watch Series 8"]
target_product_name = input("enter your product name exactly: ")
result_indices = linear_search_product(products, target_product_name)
if result_indices:
    print(f"The target product '{target_product_name}' is found at indices {result_indices}.")
else:
    print(f"The target product '{target_product_name}' is not found.")
