def generate_links():
    """Generate 20 links from megalinks.txt."""
    
    links = []
    with open("megalinks.txt", "r") as f:
        for i, line in enumerate(f, 1):
            url = line.strip()  # Remove any newline or whitespace from the link
            links.append(f'<a href="{url}">Link {i}</a><br>')
            if i == 20:  # Stop after 20 links
                break
    
    return "\n".join(links)

def update_html_template():
    with open("index.html", "r") as f:
        template = f.read()

    new_links = generate_links()
    modified_html = template.replace("{{links}}", new_links)
    
    with open("index.html", "w") as f:
        f.write(modified_html)

if __name__ == "__main__":
    update_html_template()