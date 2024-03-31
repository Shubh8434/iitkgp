
import streamlit as st
import pandas as pd

# Load the CSV files containing the list of YouTube video links, chapters, and structures
@st.cache_data
def load_data(video_csv, chapter_csv, structure_csv):
    df_videos = pd.read_csv(video_csv)
    df_chapters = pd.read_csv(chapter_csv)
    df_structures = pd.read_csv(structure_csv)
    return df_videos, df_chapters, df_structures

# Function to convert timestamp to seconds
def timestamp_to_seconds(timestamp):
    parts = timestamp.split(":")
    hours = int(parts[0]) * 60
    minutes = int(parts[1]) * 1
    seconds = int(parts[2]) * 0
    return hours + minutes + seconds

# Function to search for answers based on the user's question
def search_answers(df, video_link, question):
    # Filter DataFrame based on the selected video link
    video_df = df[df['video url'] == video_link]
    
    # Search for the question in the DataFrame
    result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
    if not result.empty:
        answer = {}
        if 'Answers' in result:
            answer['Answers'] = result['Answers'].iloc[0]
        else:
            answer['Answers'] = None
        
        if 'Start' in result and 'End' in result:
            answer['Start'] = result['Start'].iloc[0]
            answer['End'] = result['End'].iloc[0]
        else:
            answer['Start'] = None
            answer['End'] = None
        
        if 'Categories' in result:
            answer['Categories'] = result['Categories'].iloc[0]
        else:
            answer['Categories'] = None
        
        return answer
    else:
        return None

def main():

    # Load the CSV files
    df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")
    st.title('Educational Video Assistant')
    # Text input for pasting YouTube video link
    video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

    # Process button to trigger further actions
    if st.button("Process"):
        # You can add any processing logic here
        st.write("Processing...")

    # Display the selected video title above the video player
    if video_link:
        video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
        st.write(f"Video Title: {video_title}")

        # Display the selected video
        st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

        # Text input for questions
        question = st.text_input("Enter your question")

        # Search for answers based on the selected video link and the entered question
        if st.button("Get Answer"):
            # Search for answers
            answer = search_answers(df_videos, video_link, question)
            # Display the answer if available
            if answer is not None:
                st.write("Answer:")
                if answer['Answers'] is not None:
                    st.write(f"Answer: {answer['Answers']}")
                else:
                    st.write("No answer found.")
                
                if answer['Start'] is not None and answer['End'] is not None:
                    start_seconds = timestamp_to_seconds(answer['Start'])
                    end_seconds = timestamp_to_seconds(answer['End'])
                    st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
                    st.write(f"End: {answer['End']} (seconds: {end_seconds})")
                    st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                
                # if answer['Categories'] is not None:
                #     st.write(f"Categories: {answer['Categories']}")
            else:
                st.write("No answer found for the question.")

    # Display sidebar with chapters
    chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
    st.sidebar.header("Chapters")
    for index, row in chapters_df.iterrows():
        chapter_start_seconds = timestamp_to_seconds(row['start'])
        chapter_end_seconds = timestamp_to_seconds(row['end'])
        chapter_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={chapter_start_seconds}&end={chapter_end_seconds}">{row["chapter"]}</a>'
        st.sidebar.write(chapter_link, unsafe_allow_html=True)

    # Display sidebar with structures
    structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
    st.sidebar.header("Structures")
    for index, row in structures_df.iterrows():
        structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
        structure_end_seconds = timestamp_to_seconds(row['end'])
        structure_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={structure_start_seconds}&end={structure_end_seconds}">{row["structure_"]}</a>'
        st.sidebar.write(structure_link, unsafe_allow_html=True)

    # Print DataFrame for debugging
    # st.write("DataFrame:")
    # st.write(df_videos)

if __name__ == "__main__":
    main()
