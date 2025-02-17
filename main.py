from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def get_user_input(prompt_text):
    return input(prompt_text)

def generate_story(model, theme, genre, setting, story_so_far, end_story=False):
    prompt_text = """
    Write a story based on the following details:
    Theme: {theme}
    Genre: {genre}
    Setting: {setting}
    Story so far: {story_so_far}
    """
    
    if end_story:
        prompt_text += "\nProvide a satisfying ending to the story."
    else:
        prompt_text += "\nContinue the story in an engaging and creative way."
    
    prompt = ChatPromptTemplate.from_template(prompt_text)
    response = model.invoke(
        prompt.format(theme=theme, genre=genre, setting=setting, story_so_far=story_so_far)
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
        user_decision = get_user_input("What happens next? (type 'continue' to keep going, 'end' to conclude): ")
        
        if user_decision.lower() == 'end':
            story_part = generate_story(model, theme, genre, setting, story, end_story=True)
            print(story_part)
            print("\nThe story has concluded.")
            break
        
        story_part = generate_story(model, theme, genre, setting, story)
        print(story_part)
        story += " " + story_part


if __name__ == "__main__":
    interactive_story()
