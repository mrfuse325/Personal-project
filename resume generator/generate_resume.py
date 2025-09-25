import json
from jinja2 import Environment, FileSystemLoader

def generate_resume():
    # Load resume data
    with open("resume.json", "r") as f:
        data = json.load(f)

    # Load Jinja2 environment
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    # Render template with JSON data
    output = template.render(data)

    # Save to HTML file
    with open("resume.html", "w", encoding="utf-8") as f:
        f.write(output)

    print("✅ Resume generated successfully! Open resume.html in your browser.")

if __name__ == "__main__":
    generate_resume()
