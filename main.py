from bs4 import BeautifulSoup


html = """
<div class="product">
  <h2>Product Title</h2>
  <div class="price">
    <span class="discount">12.99</span>
    <span class="full">19.99</span>
  </div>
</div>
"""



soup = BeautifulSoup(html, 'html.parser')


product = {
    "title": soup.find("span").text,
}

print(product)