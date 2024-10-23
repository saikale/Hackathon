import openai

# Set up your OpenAI API key
openai.api_key = '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'
def read_transcript(file_path):
    """Reads the interview transcript from a notepad file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            transcript = file.read()
        return transcript
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"Error: {str(e)}"

def get_feedback_from_chatgpt(transcript):
    """Sends the transcript to ChatGPT for interview feedback."""
    try:
        # Send a request to ChatGPT with the newer model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated to the newer model
            messages=[
                {"role": "system", "content": "You are a helpful assistant providing interview feedback."},
                {"role": "user", "content": f"Provide feedback for this interview transcript:\n\n{transcript}"}
            ],
            max_tokens=500,  # Adjust based on desired feedback length
            temperature=0.7,  # Control creativity; you can adjust this
        )
        # Extract and return the generated feedback
        feedback = response['choices'][0]['message']['content'].strip()
        return feedback
    except Exception as e:
        return f"Error during API call: {str(e)}"

def save_feedback(feedback, output_file):
    """Saves the feedback to a text file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(feedback)
        return f"Feedback saved to {output_file}"
    except Exception as e:
        return f"Error saving feedback: {str(e)}"

# Main function to process the interview transcript
def process_interview_feedback(input_file, output_file):
    # Step 1: Read transcript from the input file
    transcript = read_transcript(input_file)
    
    if "Error" in transcript:
        print(transcript)
        return
    
    # Step 2: Get feedback from ChatGPT
    feedback = get_feedback_from_chatgpt(transcript)
    
    if "Error" in feedback:
        print(feedback)
        return
    
    # Step 3: Save the feedback to an output file
    result = save_feedback(feedback, output_file)
    print(result)

# Example usage
if __name__ == "__main__":
    input_file = r'C:\Users\Admin\interview_transcript.txt'  # Replace with your input file path
    output_file = r'C:\Users\Admin\interview_feedback.txt'   # Replace with your output file path
    process_interview_feedback(input_file, output_file)
