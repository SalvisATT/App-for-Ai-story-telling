from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def get_user_input(prompt_text):
    return input(prompt_text)

def generate_story(model, theme, genre, setting, story_so_far, user_input, end_story=False):
    prompt_text = """
    Write a story based on the following details:
    Theme: {theme}
    Genre: {genre}
    Setting: {setting}
    Story so far: {story_so_far}
    User input: {user_input}
    """
    
    if end_story:
        prompt_text += "\nProvide a satisfying ending to the story."
    else:
        prompt_text += "\nIncorporate the user's input and continue the story in an engaging and creative way."
    
    prompt = ChatPromptTemplate.from_template(prompt_text)
    response = model.invoke(
        prompt.format(theme=theme, genre=genre, setting=setting, story_so_far=story_so_far, user_input=user_input), max_tokens = 200
    )
    return response

def interactive_story():
    model = OllamaLLM(model="mistral")
    
    theme = get_user_input("Enter the theme of the story: ")
    genre = get_user_input("Enter the genre of the story: ")
    setting = get_user_input("Where does the story take place? ")
    
    print("\nGenerating story...\n")
    story = ""
    
    while True:
        user_input = get_user_input("What happens next? (type 'end' to conclude): ")
        
        if user_input.lower() == 'end':
            story_part = generate_story(model, theme, genre, setting, story, user_input, end_story=True)
            print(story_part)
            print("\nThe story has concluded.")
            break
        
        story_part = generate_story(model, theme, genre, setting, story, user_input)
        print(story_part)
        story += " " + user_input + " " + story_part


if __name__ == "__main__":
    interactive_story()
