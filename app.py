# # import streamlit as st
# # import pandas as pd

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # def main():
# #     st.title("YouTube Video Player")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video with reduced width
# #     with st.sidebar:
# #         st.write("Select a YouTube video")
# #         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video
# #     st.sidebar.write(f"You selected: {selected_video}")
# #     st.sidebar.subheader("Video Player")
# #     st.sidebar.write(f"YouTube Video Embed:")
# #     st.sidebar.write(f'<iframe width="510" height="315" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# # if __name__ == "__main__":
# #     main()


# # import streamlit as st
# # import pandas as pd

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         return result[['Answers', 'Categories']].iloc[0]
# #     else:
# #         return None

# # def main():
# #     st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video with reduced width
# #     with st.sidebar:
# #         st.write("Select a YouTube video")
# #         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video
# #     st.sidebar.write(f"You selected: {selected_video}")
# #     st.sidebar.subheader("Video Player")
# #     st.sidebar.write(f"YouTube Video Embed:")
# #     st.sidebar.write(f'<iframe width="510" height="315" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
        
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if 'Answers' in answer:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
                
# #             if 'Categories' in answer:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame columns for debugging
# #     st.write("DataFrame Columns:")
# #     st.write(df.columns)

# # if __name__ == "__main__":
# #     main()
# # import streamlit as st
# # import pandas as pd

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         # Debugging print
# #         print("Result DataFrame:")
# #         print(result)
        
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video with reduced width
# #     with st.sidebar:
# #         st.write("Select a YouTube video")
# #         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video
# #     st.sidebar.write(f"You selected: {selected_video}")
# #     st.sidebar.subheader("Video Player")
# #     st.sidebar.write(f"YouTube Video Embed:")
# #     st.sidebar.write(f'<iframe width="510" height="315" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         print(answer)
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 st.write(f"Start: {answer['Start']}")
# #                 st.write(f"End: {answer['End']}")
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     st.write("DataFrame:")
# #     st.write(df)

# # if __name__ == "__main__":
# #     main()

# # import streamlit as st
# # import pandas as pd

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         # Debugging print
# #         print("Result DataFrame:")
# #         print(result)
        
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Set sidebar width
# #     st.markdown(
# #         """
# #         <style>
# #             .sidebar .sidebar-content {
# #                 width: 100px !important;
# #             }
# #         </style>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     # Set dropdown width
# #     st.markdown(
# #         """
# #         <style>
# #             .dropdown .dropdown-content {
# #                 width: 100px !important;
# #             }
# #         </style>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     # Create a dropdown menu to select a video with reduced width
# #     with st.sidebar:
# #         st.write("Select a YouTube video")
# #         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

# #         # Get the corresponding video title
# #         video_title = df[df['video url'] == selected_video]['title'].iloc[0]
# #         st.write(f"Video Title: {video_title}")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video
# #     st.sidebar.subheader("Video Player")
# #     # st.sidebar.write(f"YouTube Video Embed:")
# #     st.sidebar.write(f'<iframe width="460" height="250" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         # Display the answer if available
# #         if answer is not None:
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 st.write(f"Start: {answer['Start']}")
# #                 st.write(f"End: {answer['End']}")
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     # st.write("DataFrame:")
# #     # st.write(df)

# # if __name__ == "__main__":
# #     main()


# # import streamlit as st
# # import pandas as pd
# # import re

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to convert timestamp to seconds
# # def timestamp_to_seconds(timestamp):
# #     parts = timestamp.split(":")
# #     hours = int(parts[0]) * 60
# #     minutes = int(parts[1]) * 1
# #     seconds = int(parts[2]) * 0
# #     return hours + minutes + seconds

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Set sidebar width
# #     st.markdown(
# #         """
# #         <style>
# #             .sidebar .sidebar-content {
# #                 width: 150px !important;
# #             }
# #         </style>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     # Set dropdown width
# #     st.markdown(
# #         """
# #         <style>
# #             .dropdown .dropdown-content {
# #                 width: 150px !important;
# #             }
# #         </style>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     # Create a dropdown menu to select a video with reduced width
# #     with st.sidebar:
# #         # st.write("Select a YouTube video")
# #         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video title above the video player
# #     video_title = df[df['video url'] == video_link]['title'].iloc[0]
# #     st.sidebar.write(f"Video Title: {video_title}")

# #     # Display the selected video
# #     # st.sidebar.subheader("Video Player")
# #     st.sidebar.write(f"Video Player")
    
# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 start_seconds = timestamp_to_seconds(answer['Start'])
# #                 end_seconds = timestamp_to_seconds(answer['End'])
# #                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
# #                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
# #                 st.sidebar.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     st.write("DataFrame:")
# #     st.write(df)

# # if __name__ == "__main__":
# #     main()


# # import streamlit as st
# # import pandas as pd
# # import re

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to convert timestamp to seconds
# # def timestamp_to_seconds(timestamp):
# #     parts = timestamp.split(":")
# #     hours = int(parts[0]) * 3600
# #     minutes = int(parts[1]) * 60
# #     seconds = int(parts[2])
# #     return hours + minutes + seconds

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video
# #     selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video title above the video player
# #     video_title = df[df['video url'] == video_link]['title'].iloc[0]
# #     st.write(f"Video Title: {video_title}")

# #     # Display the selected video
# #     st.write(f"Video Player")
# #     st.write(f'<iframe width="650" height="400" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 start_seconds = timestamp_to_seconds(answer['Start'])
# #                 end_seconds = timestamp_to_seconds(answer['End'])
# #                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
# #                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
# #                 st.write(f'<iframe width="550" height="450" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     st.write("DataFrame:")
# #     st.write(df)

# # if __name__ == "__main__":
# #     main()

# # import streamlit as st
# # import pandas as pd
# # import re

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to convert timestamp to seconds
# # def timestamp_to_seconds(timestamp):
# #     parts = timestamp.split(":")
# #     hours = int(parts[0]) * 60
# #     minutes = int(parts[1]) * 1
# #     seconds = int(parts[2]) * 0
# #     return hours + minutes + seconds

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     # st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video
# #     selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video title above the video player
# #     video_title = df[df['video url'] == video_link]['title'].iloc[0]
# #     st.write(f"Video Title: {video_title}")

# #     # Display the selected video
# #     st.write(f"Video Player")
# #     st.write(f'<iframe width="700" height="350" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 start_seconds = timestamp_to_seconds(answer['Start'])
# #                 end_seconds = timestamp_to_seconds(answer['End'])
# #                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
# #                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
# #                 st.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     st.write("DataFrame:")
# #     st.write(df)

# # if __name__ == "__main__":
# #     main()


# # import streamlit as st
# # import pandas as pd
# # import re

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to convert timestamp to seconds
# # def timestamp_to_seconds(timestamp):
# #     parts = timestamp.split(":")
# #     hours = int(parts[0]) * 60
# #     minutes = int(parts[1]) * 1
# #     seconds = int(parts[2]) 
# #     return hours + minutes + seconds

# # # Function to generate link for timestamp
# # def generate_timestamp_link(video_link, timestamp):
# #     seconds = timestamp_to_seconds(timestamp)
# #     return f'<a href="https://www.youtube.com/watch?v={video_link.split("=")[-1]}&t={seconds}s" target="_blank">{timestamp}</a>'

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     # st.title("YouTube Video Player and Database Query")

# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video
# #     selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video title above the video player
# #     video_title = df[df['video url'] == video_link]['title'].iloc[0]
# #     st.write(f"Video Title: {video_title}")

# #     # Display the selected video
# #     st.write(f"Video Player")
# #     st.write(f'<iframe width="700" height="350" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 start_link = generate_timestamp_link(video_link, answer['Start'])
# #                 end_link = generate_timestamp_link(video_link, answer['End'])
# #                 st.markdown(f"Start: {start_link} (click to jump to this timestamp)", unsafe_allow_html=True)
# #                 st.markdown(f"End: {end_link} (click to jump to this timestamp)", unsafe_allow_html=True)
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     st.write("DataFrame:")
# #     st.write(df)

# # if __name__ == "__main__":
# #     main()

# # import streamlit as st
# # import pandas as pd

# # # Load the CSV file containing the list of YouTube video links
# # @st.cache_data
# # def load_data(csv_file):
# #     df = pd.read_csv(csv_file)
# #     return df

# # # Function to convert timestamp to seconds
# # def timestamp_to_seconds(timestamp):
# #     parts = timestamp.split(":")
# #     hours = int(parts[0]) * 60
# #     minutes = int(parts[1]) * 1
# #     seconds = int(parts[2]) * 0
# #     return hours + minutes + seconds

# # # Function to generate link for timestamp
# # def generate_timestamp_link(video_link, timestamp):
# #     seconds = timestamp_to_seconds(timestamp)
# #     minutes = seconds // 60
# #     seconds %= 60
# #     return f'<a href="#t={minutes}m{seconds}s">{timestamp}</a>'

# # # Function to search for answers based on the user's question
# # def search_answers(df, video_link, question):
# #     # Filter DataFrame based on the selected video link
# #     video_df = df[df['video url'] == video_link]
    
# #     # Search for the question in the DataFrame
# #     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
# #     if not result.empty:
# #         answer = {}
# #         if 'Answers' in result:
# #             answer['Answers'] = result['Answers'].iloc[0]
# #         else:
# #             answer['Answers'] = None
        
# #         if 'Start' in result and 'End' in result:
# #             answer['Start'] = result['Start'].iloc[0]
# #             answer['End'] = result['End'].iloc[0]
# #         else:
# #             answer['Start'] = None
# #             answer['End'] = None
        
# #         if 'Categories' in result:
# #             answer['Categories'] = result['Categories'].iloc[0]
# #         else:
# #             answer['Categories'] = None
        
# #         return answer
# #     else:
# #         return None

# # def main():
# #     # Load the CSV file
# #     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

# #     # Filter out duplicate video links
# #     unique_video_links = df['video url'].unique()

# #     # Create a dropdown menu to select a video
# #     selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, help="You can select a YouTube video from the dropdown menu")

# #     # Get the corresponding video link from the DataFrame
# #     video_link = selected_video

# #     # Display the selected video title above the video player
# #     video_title = df[df['video url'] == video_link]['title'].iloc[0]
# #     st.write(f"Video Title: {video_title}")

# #     # Display the selected video
# #     st.write(f"Video Player")
# #     st.write(f'<iframe width="700" height="350" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# #     # Text input for questions
# #     question = st.text_input("Enter your question")

# #     # Search for answers based on the selected video link and the entered question
# #     if st.button("Get Answer"):
# #         # Search for answers
# #         answer = search_answers(df, video_link, question)
# #         # Display the answer if available
# #         if answer is not None:
# #             st.write("Answer:")
# #             if answer['Answers'] is not None:
# #                 st.write(f"Answer: {answer['Answers']}")
# #             else:
# #                 st.write("No answer found.")
            
# #             if answer['Start'] is not None and answer['End'] is not None:
# #                 start_link = generate_timestamp_link(video_link, answer['Start'])
# #                 end_link = generate_timestamp_link(video_link, answer['End'])
# #                 st.markdown(f"Start: {start_link} (click to jump to this timestamp)", unsafe_allow_html=True)
# #                 st.markdown(f"End: {end_link} (click to jump to this timestamp)", unsafe_allow_html=True)
            
# #             if answer['Categories'] is not None:
# #                 st.write(f"Categories: {answer['Categories']}")
# #         else:
# #             st.write("No answer found for the question.")

# #     # Print DataFrame for debugging
# #     st.write("DataFrame:")
# #     st.write(df)

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# import pandas as pd

# # Load the CSV file containing the list of YouTube video links
# @st.cache
# def load_data(csv_file):
#     df = pd.read_csv(csv_file)
#     return df

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():
#     st.title("YouTube Video Player and Database Query")

#     # Load the CSV file
#     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

#     # Filter out duplicate video links
#     unique_video_links = df['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Set dropdown width
#     st.markdown(
#         """
#         <style>
#             .dropdown .dropdown-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create a dropdown menu to select a video with reduced width
#     with st.sidebar:
#         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df[df['video url'] == video_link]['title'].iloc[0]
#     st.sidebar.write(f"Video Title: {video_title}")

#     # Display the selected video
#     st.sidebar.write(f"Video Player")
#     st.write(f'<iframe id="videoPlayer" width="700" height="350" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#     # Text input for questions
#     question = st.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if st.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             st.write("Answer:")
#             if answer['Answers'] is not None:
#                 st.write(f"Answer: {answer['Answers']}")
#             else:
#                 st.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 st.sidebar.video(f"https://www.youtube.com/embed/{video_link.split('=')[-1]}?start={start_seconds}&end={end_seconds}")
            
#             if answer['Categories'] is not None:
#                 st.write(f"Categories: {answer['Categories']}")
#         else:
#             st.write("No answer found for the question.")

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pandas as pd
# import re

# # Load the CSV file containing the list of YouTube video links
# @st.cache_data
# def load_data(csv_file):
#     df = pd.read_csv(csv_file)
#     return df

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV file
#     df = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv")

#     # Filter out duplicate video links
#     unique_video_links = df['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Set dropdown width
#     st.markdown(
#         """
#         <style>
#             .dropdown .dropdown-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create a dropdown menu to select a video with reduced width
#     with st.sidebar:
#         # st.write("Select a YouTube video")
#         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df[df['video url'] == video_link]['title'].iloc[0]
#     st.sidebar.write(f"Video Title: {video_title}")

#     # Display the selected video
#     # st.sidebar.subheader("Video Player")
#     st.sidebar.write(f"Video Player")
#     # st.write(f'<iframe id="videoPlayer" width="300" height="350" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
#     # Text input for questions
#     question = st.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if st.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             st.write("Answer:")
#             if answer['Answers'] is not None:
#                 st.write(f"Answer: {answer['Answers']}")
#             else:
#                 st.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 st.sidebar.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
#             if answer['Categories'] is not None:
#                 st.write(f"Categories: {answer['Categories']}")
#         else:
#             st.write("No answer found for the question.")

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links and chapters
# @st.cache_data
# def load_data(video_csv, chapter_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     return df_videos, df_chapters

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 3600
#     minutes = int(parts[1]) * 60
#     seconds = int(parts[2])
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv")

#     # Filter out duplicate video links
#     unique_video_links = df_videos['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Set dropdown width
#     st.markdown(
#         """
#         <style>
#             .dropdown .dropdown-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create a dropdown menu to select a video with reduced width
#     with st.sidebar:
#         selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#     st.sidebar.write(f"Video Title: {video_title}")

#     # Display the selected video
#     st.sidebar.write(f"Video Player")

#     # Text input for questions
#     question = st.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if st.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df_videos, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             st.write("Answer:")
#             if answer['Answers'] is not None:
#                 st.write(f"Answer: {answer['Answers']}")
#             else:
#                 st.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 st.sidebar.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
#             if answer['Categories'] is not None:
#                 st.write(f"Categories: {answer['Categories']}")
#         else:
#             st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("chapter")
#     for index, row in chapters_df.iterrows():
#         st.sidebar.write(f"{row['chapter']} - start: {row['start']}, end: {row['end']}")

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links and chapters
# @st.cache_data
# def load_data(video_csv, chapter_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     return df_videos, df_chapters

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv")

#     # Filter out duplicate video links
#     unique_video_links = df_videos['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 150px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create a dropdown menu to select a video with reduced width
#     selected_video = st.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#     st.write(f"Video Title: {video_title}")

#     # Display the selected video
#     # st.write(f"Video Player")
#     # st.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#     # Text input for questions
#     question = st.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if st.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df_videos, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             st.write("Answer:")
#             if answer['Answers'] is not None:
#                 st.write(f"Answer: {answer['Answers']}")
#             else:
#                 st.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 st.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
#             if answer['Categories'] is not None:
#                 st.write(f"Categories: {answer['Categories']}")
#         else:
#             st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         st.sidebar.write(f"{row['chapter']} - Start: {row['start']}, End: {row['end']}")

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links and chapters
# @st.cache_data
# def load_data(video_csv, chapter_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     return df_videos, df_chapters

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv")

#     # Filter out duplicate video links
#     unique_video_links = df_videos['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 200px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create two columns layout
#     col1, col2 = st.columns([1, 2])

#     # Create a dropdown menu to select a video
#     selected_video = col1.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#     col1.write(f"Video Title: {video_title}")

#     # Display the selected video
#     col1.write(f"Video Player")
#     col1.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#     # Text input for questions
#     question = col2.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if col2.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df_videos, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             col2.write("Answer:")
#             if answer['Answers'] is not None:
#                 col2.write(f"Answer: {answer['Answers']}")
#             else:
#                 col2.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 col2.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 col2.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 col2.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
#             if answer['Categories'] is not None:
#                 col2.write(f"Categories: {answer['Categories']}")
#         else:
#             col2.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         st.sidebar.write(f"{row['chapter']} - Start: {row['start']}, End: {row['end']}")

#     # Print DataFrame for debugging
#     col2.write("DataFrame:")
#     col2.write(df_videos)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links and chapters
# @st.cache_data
# def load_data(video_csv, chapter_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     return df_videos, df_chapters

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv")

#     # Filter out duplicate video links
#     unique_video_links = df_videos['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 50px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create two columns layout
#     col1, col2 = st.columns([2, 3])

#     # Create a dropdown menu to select a video
#     selected_video = col1.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#     col1.write(f"Video Title: {video_title}")

#     # Display the selected video
#     col1.write(f"Video Player")
#     col1.write(f'<iframe width="250" height="150" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#     # Text input for questions
#     question = col2.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if col2.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df_videos, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             col2.write("Answer:")
#             if answer['Answers'] is not None:
#                 col2.write(f"Answer: {answer['Answers']}")
#             else:
#                 col2.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 col2.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
#                 col2.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 col2.write(f"End: {answer['End']} (seconds: {end_seconds})")
            
#             if answer['Categories'] is not None:
#                 col2.write(f"Categories: {answer['Categories']}")
#         else:
#             col2.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         st.sidebar.write(f"{row['chapter']} - Start: {row['start']}, End: {row['end']}")

#     # Print DataFrame for debugging
#     col2.write("DataFrame:")
#     col2.write(df_videos)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links and chapters
# @st.cache_data
# def load_data(video_csv, chapter_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     return df_videos, df_chapters

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv")

#     # Filter out duplicate video links
#     unique_video_links = df_videos['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 100px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create two columns layout
#     col1, col2 = st.columns([5,3],gap="large")

#     # Create a dropdown menu to select a video
#     selected_video = col1.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#     col1.write(f"Video Title: {video_title}")
#     col1.write(f'<iframe width="400" height="250" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
#     # Display the selected video
#     # st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#     # Text input for questions
#     question = col2.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if col2.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df_videos, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             col2.write("Answer:")
#             if answer['Answers'] is not None:
#                 col2.write(f"Answer: {answer['Answers']}")
#             else:
#                 col2.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 col2.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 col2.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 col1.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
#             if answer['Categories'] is not None:
#                 col2.write(f"Categories: {answer['Categories']}")
#         else:
#             col2.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={chapter_start_seconds}&end={chapter_end_seconds}">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     col2.write("DataFrame:")
#     col2.write(df_videos)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links, chapters, and structures
# @st.cache_data
# def load_data(video_csv, chapter_csv, structure_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     df_structures = pd.read_csv(structure_csv)
#     return df_videos, df_chapters, df_structures

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")

#     # Filter out duplicate video links
#     unique_video_links = df_videos['video url'].unique()

#     # Set sidebar width
#     st.markdown(
#         """
#         <style>
#             .sidebar .sidebar-content {
#                 width: 200px !important;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create a dropdown menu to select a video
#     selected_video = st.sidebar.selectbox("Select a YouTube video", unique_video_links, format_func=lambda x: x, key='dropdown', help="You can select a YouTube video from the dropdown menu")

#     # Get the corresponding video link from the DataFrame
#     video_link = selected_video

#     # Display the selected video title above the video player
#     video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#     st.write(f"Video Title: {video_title}")

#     # Display the selected video
#     st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#     # Text input for questions
#     question = st.text_input("Enter your question")

#     # Search for answers based on the selected video link and the entered question
#     if st.button("Get Answer"):
#         # Search for answers
#         answer = search_answers(df_videos, video_link, question)
#         # Display the answer if available
#         if answer is not None:
#             st.write("Answer:")
#             if answer['Answers'] is not None:
#                 st.write(f"Answer: {answer['Answers']}")
#             else:
#                 st.write("No answer found.")
            
#             if answer['Start'] is not None and answer['End'] is not None:
#                 start_seconds = timestamp_to_seconds(answer['Start'])
#                 end_seconds = timestamp_to_seconds(answer['End'])
#                 st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                 st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                 st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
#             if answer['Categories'] is not None:
#                 st.write(f"Categories: {answer['Categories']}")
#         else:
#             st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={chapter_start_seconds}&end={chapter_end_seconds}">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Display sidebar with structures
#     structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
#     st.sidebar.header("Structures")
#     for index, row in structures_df.iterrows():
#         structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
#         structure_end_seconds = timestamp_to_seconds(row['end'])
#         structure_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={structure_start_seconds}&end={structure_end_seconds}">{row["structure_"]}</a>'
#         st.sidebar.write(structure_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links, chapters, and structures
# @st.cache_data
# def load_data(video_csv, chapter_csv, structure_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     df_structures = pd.read_csv(structure_csv)
#     return df_videos, df_chapters, df_structures

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")
#     st.title('Educational Video Assistant')
#     # Text input for pasting YouTube video link
#     video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

#     # Display the selected video title above the video player
#     if video_link:
#         video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#         st.write(f"Video Title: {video_title}")

#         # Display the selected video
#         st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#         # Text input for questions
#         question = st.text_input("Enter your question")

#         # Search for answers based on the selected video link and the entered question
#         if st.button("Get Answer"):
#             # Search for answers
#             answer = search_answers(df_videos, video_link, question)
#             # Display the answer if available
#             if answer is not None:
#                 st.write("Answer:")
#                 if answer['Answers'] is not None:
#                     st.write(f"Answer: {answer['Answers']}")
#                 else:
#                     st.write("No answer found.")
                
#                 if answer['Start'] is not None and answer['End'] is not None:
#                     start_seconds = timestamp_to_seconds(answer['Start'])
#                     end_seconds = timestamp_to_seconds(answer['End'])
#                     st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                     st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                     st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                
#                 if answer['Categories'] is not None:
#                     st.write(f"Categories: {answer['Categories']}")
#             else:
#                 st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={chapter_start_seconds}&end={chapter_end_seconds}">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Display sidebar with structures
#     structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
#     st.sidebar.header("Structures")
#     for index, row in structures_df.iterrows():
#         structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
#         structure_end_seconds = timestamp_to_seconds(row['end'])
#         structure_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={structure_start_seconds}&end={structure_end_seconds}">{row["structure_"]}</a>'
#         st.sidebar.write(structure_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links, chapters, and structures
# @st.cache_data
# def load_data(video_csv, chapter_csv, structure_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     df_structures = pd.read_csv(structure_csv)
#     return df_videos, df_chapters, df_structures

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")
#     st.title('Educational Video Assistant')
#     # Text input for pasting YouTube video link
#     video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

#     # Process button to trigger further actions
#     if st.button("Process"):
#         # You can add any processing logic here
#         st.write("Processing...")

#     # Display the selected video title above the video player
#     if video_link:
#         video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#         st.write(f"Video Title: {video_title}")

#         # Display the selected video
#         st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#         # Text input for questions
#         question = st.text_input("Enter your question")

#         # Search for answers based on the selected video link and the entered question
#         if st.button("Get Answer"):
#             # Search for answers
#             answer = search_answers(df_videos, video_link, question)
#             # Display the answer if available
#             if answer is not None:
#                 st.write("Answer:")
#                 if answer['Answers'] is not None:
#                     st.write(f"Answer: {answer['Answers']}")
#                 else:
#                     st.write("No answer found.")
                
#                 if answer['Start'] is not None and answer['End'] is not None:
#                     start_seconds = timestamp_to_seconds(answer['Start'])
#                     end_seconds = timestamp_to_seconds(answer['End'])
#                     st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                     st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                     st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                
#                 # if answer['Categories'] is not None:
#                 #     st.write(f"Categories: {answer['Categories']}")
#             else:
#                 st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={chapter_start_seconds}&end={chapter_end_seconds}">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Display sidebar with structures
#     structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
#     st.sidebar.header("Structures")
#     for index, row in structures_df.iterrows():
#         structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
#         structure_end_seconds = timestamp_to_seconds(row['end'])
#         structure_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={structure_start_seconds}&end={structure_end_seconds}">{row["structure_"]}</a>'
#         st.sidebar.write(structure_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links, chapters, and structures
# @st.cache_data
# def load_data(video_csv, chapter_csv, structure_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     df_structures = pd.read_csv(structure_csv)
#     return df_videos, df_chapters, df_structures

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")
#     st.title('Educational Video Assistant')
#     # Text input for pasting YouTube video link
#     video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

#     # Process button to trigger further actions
#     if st.button("Process"):
#         # You can add any processing logic here
#         st.write("Processing...")

#     # Display the selected video title above the video player
#     if video_link:
#         video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#         st.write(f"Video Title: {video_title}")

#         # Display the selected video
#         st.write(f'<iframe id="video_player" width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#         # Text input for questions
#         question = st.text_input("Enter your question")

#         # Search for answers based on the selected video link and the entered question
#         if st.button("Get Answer"):
#             # Search for answers
#             answer = search_answers(df_videos, video_link, question)
#             # Display the answer if available
#             if answer is not None:
#                 st.write("Answer:")
#                 if answer['Answers'] is not None:
#                     st.write(f"Answer: {answer['Answers']}")
#                 else:
#                     st.write("No answer found.")
                
#                 if answer['Start'] is not None and answer['End'] is not None:
#                     start_seconds = timestamp_to_seconds(answer['Start'])
#                     end_seconds = timestamp_to_seconds(answer['End'])
#                     st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                     st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                     st.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                
#                 # if answer['Categories'] is not None:
#                 #     st.write(f"Categories: {answer['Categories']}")
#             else:
#                 st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="#" onclick="changeVideo(\'{video_link.split("=")[-1]}\', {chapter_start_seconds}, {chapter_end_seconds});">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Display sidebar with structures
#     structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
#     st.sidebar.header("Structures")
#     for index, row in structures_df.iterrows():
#         structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
#         structure_end_seconds = timestamp_to_seconds(row['end'])
#         structure_link = f'<a href="#" onclick="changeVideo(\'{video_link.split("=")[-1]}\', {structure_start_seconds}, {structure_end_seconds});">{row["structure_"]}</a>'
#         st.sidebar.write(structure_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd

# # Load the CSV files containing the list of YouTube video links, chapters, and structures
# @st.cache_data
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
    print("hello",video_df['Questions'].dtype)
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

# def main():

#     # Load the CSV files
#     df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")
#     st.title('Educational Video Assistant')
#     # Text input for pasting YouTube video link
#     video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

#     # Process button to trigger further actions
#     if st.button("Process"):
#         # You can add any processing logic here
#         st.write("Processing...")

#     # Display the selected video title above the video player
#     if video_link:
#         video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#         st.write(f"Video Title: {video_title}")

#         # Display the selected video
#         st.write(f'<iframe id="video_player" width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#         # Text input for questions
#         question = st.text_input("Enter your question")

#         # Search for answers based on the selected video link and the entered question
#         if st.button("Get Answer"):
#             # Search for answers
#             answer = search_answers(df_videos, video_link, question)
#             # Display the answer if available
#             if answer is not None:
#                 st.write("Answer:")
#                 if answer['Answers'] is not None:
#                     st.write(f"Answer: {answer['Answers']}")
#                 else:
#                     st.write("No answer found.")
                
#                 if answer['Start'] is not None and answer['End'] is not None:
#                     start_seconds = timestamp_to_seconds(answer['Start'])
#                     end_seconds = timestamp_to_seconds(answer['End'])
#                     st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                     st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                     st.write(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                
#                 # if answer['Categories'] is not None:
#                 #     st.write(f"Categories: {answer['Categories']}")
#             else:
#                 st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="#" onclick="changeVideo(\'{video_link.split("=")[-1]}\', {chapter_start_seconds}, {chapter_end_seconds}); event.preventDefault();">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Display sidebar with structures
#     structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
#     st.sidebar.header("Structures")
#     for index, row in structures_df.iterrows():
#         structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
#         structure_end_seconds = timestamp_to_seconds(row['end'])
#         structure_link = f'<a href="#" onclick="changeVideo(\'{video_link.split("=")[-1]}\', {structure_start_seconds}, {structure_end_seconds}); event.preventDefault();">{row["structure_"]}</a>'
#         st.sidebar.write(structure_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd

# Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question (optional for your specific use case)
# def search_answers(df, video_link, question):
#     # ... (Implement your search logic here, similar to the original code)
#     pass

def main():

    # Load the CSV files (replace with your file paths)
    df_videos, df_chapters, df_structures = load_data(
        "/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv",
        "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv",
        "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv"
    )

    st.title('Educational Video Assistant')

    # Text input for pasting YouTube video link
    video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

    # Process button to trigger further actions (can be removed if not needed)
    if st.button("Process"):
        # You can add any processing logic here (if applicable)
        st.write("Processing...")

    # Display the selected video title above the video player
    if video_link:
        video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
        st.write(f"Video Title: {video_title}")

        # Create an empty placeholder for the iframe URL
        video_iframe_url = st.empty()

        # Display the initial video using the full URL
        video_iframe_url.write(f'<iframe id="video_player" width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

        # Text input for questions (optional)
        question = st.text_input("Enter your question")

        # Search for answers based on the selected video link and the entered question (optional)
        if st.button("Get Answer"):
            answer = search_answers(df_videos, video_link, question)
            # ... (Process the answer as needed)

        # Display sidebar with chapters
        chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
        st.sidebar.header("Chapters")
        for index, row in chapters_df.iterrows():
            chapter_start_seconds = timestamp_to_seconds(row['start'])
            chapter_end_seconds = timestamp_to_seconds(row['end'])

            # Create anchor tag with JavaScript function call (without unsafe_allow_html)
            chapter_link = st.sidebar.button(
                row["chapter"],
                key=f"chapter_button_{index}",
                on_click=f"changeVideo('{video_link.split('=')[-1]}', {chapter_start_seconds}, {chapter_end_seconds})",
            )

        # Display sidebar with structures (optional for your specific use case)
        # ... (Implement similar logic for structures if needed)

# ... (Other code remains the same)
#  Print DataFrame for debugging
    st.write("DataFrame:")
    st.write(df_videos)

if __name__ == "__main__":
    main()




# import streamlit as st
# import pandas as pd

# # Load the CSV files containing the list of YouTube video links, chapters, and structures
# @st.cache_data
# def load_data(video_csv, chapter_csv, structure_csv):
#     df_videos = pd.read_csv(video_csv)
#     df_chapters = pd.read_csv(chapter_csv)
#     df_structures = pd.read_csv(structure_csv)
#     return df_videos, df_chapters, df_structures

# # Function to convert timestamp to seconds
# def timestamp_to_seconds(timestamp):
#     parts = timestamp.split(":")
#     hours = int(parts[0]) * 60
#     minutes = int(parts[1]) * 1
#     seconds = int(parts[2]) * 0
#     return hours + minutes + seconds

# # Function to search for answers based on the user's question
# def search_answers(df, video_link, question):
#     # Filter DataFrame based on the selected video link
#     video_df = df[df['video url'] == video_link]
    
#     # Search for the question in the DataFrame
#     result = video_df[video_df['Questions'].str.contains(question, case=False, na=False)]
    
#     if not result.empty:
#         answer = {}
#         if 'Answers' in result:
#             answer['Answers'] = result['Answers'].iloc[0]
#         else:
#             answer['Answers'] = None
        
#         if 'Start' in result and 'End' in result:
#             answer['Start'] = result['Start'].iloc[0]
#             answer['End'] = result['End'].iloc[0]
#         else:
#             answer['Start'] = None
#             answer['End'] = None
        
#         if 'Categories' in result:
#             answer['Categories'] = result['Categories'].iloc[0]
#         else:
#             answer['Categories'] = None
        
#         return answer
#     else:
#         return None

# def main():

#     # Load the CSV files
#     df_videos, df_chapters, df_structures = load_data("/Users/shubhamsharma/Desktop/Vscode/demo/final3.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final1.csv", "/Users/shubhamsharma/Desktop/Vscode/demo/final2.csv")
#     st.title('Educational Video Assistant')
#     # Text input for pasting YouTube video link
#     video_link = st.text_input("Paste YouTube video link", help="Paste the YouTube video link here")

#     # Process button to trigger further actions
#     if st.button("Process"):
#         # You can add any processing logic here
#         st.write("Processing...")

#     # Display the selected video title above the video player
#     if video_link:
#         video_title = df_videos[df_videos['video url'] == video_link]['title'].iloc[0]
#         st.write(f"Video Title: {video_title}")

#         # Display the selected video
#         st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#         # Text input for questions
#         question = st.text_input("Enter your question")

#         # Search for answers based on the selected video link and the entered question
#         if st.button("Get Answer"):
#             # Search for answers
#             answer = search_answers(df_videos, video_link, question)
#             # Display the answer if available
#             if answer is not None:
#                 st.write("Answer:")
#                 if answer['Answers'] is not None:
#                     st.write(f"Answer: {answer['Answers']}")
#                 else:
#                     st.write("No answer found.")
                
#                 if answer['Start'] is not None and answer['End'] is not None:
#                     start_seconds = timestamp_to_seconds(answer['Start'])
#                     end_seconds = timestamp_to_seconds(answer['End'])
#                     st.write(f"Start: {answer['Start']} (seconds: {start_seconds})")
#                     st.write(f"End: {answer['End']} (seconds: {end_seconds})")
#                     st.markdown(f'<iframe width="450" height="300" src="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={start_seconds}&end={end_seconds}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                
#                 # if answer['Categories'] is not None:
#                 #     st.write(f"Categories: {answer['Categories']}")
#             else:
#                 st.write("No answer found for the question.")

#     # Display sidebar with chapters
#     chapters_df = df_chapters[df_chapters['video url'] == video_link][['start', 'end', 'chapter']]
#     st.sidebar.header("Chapters")
#     for index, row in chapters_df.iterrows():
#         chapter_start_seconds = timestamp_to_seconds(row['start'])
#         chapter_end_seconds = timestamp_to_seconds(row['end'])
#         chapter_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={chapter_start_seconds}&end={chapter_end_seconds}">{row["chapter"]}</a>'
#         st.sidebar.write(chapter_link, unsafe_allow_html=True)

#     # Display sidebar with structures
#     structures_df = df_structures[df_structures['video url'] == video_link][['structure_', 'structure_segments', 'end']]
#     st.sidebar.header("Structures")
#     for index, row in structures_df.iterrows():
#         structure_start_seconds = timestamp_to_seconds(row['structure_segments'])
#         structure_end_seconds = timestamp_to_seconds(row['end'])
#         structure_link = f'<a href="https://www.youtube.com/embed/{video_link.split("=")[-1]}?start={structure_start_seconds}&end={structure_end_seconds}">{row["structure_"]}</a>'
#         st.sidebar.write(structure_link, unsafe_allow_html=True)

#     # Print DataFrame for debugging
#     st.write("DataFrame:")
#     st.write(df_videos)

# if __name__ == "__main__":
#     main()