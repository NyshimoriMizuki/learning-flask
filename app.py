import website


if __name__ == "__main__":
    blog = website.create_site()
    blog.run(debug=True)
