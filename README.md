A lightweight web search agent built with the Gradio SDK, capable of performing web searches, fetching important events, and retrieving current times from various timezones. This agent leverages custom tools for efficient information retrieval.

Overview
This Web Search Agent uses the Gradio SDK (version 5.15.0) to create a simple, powerful interface for performing web searches, event retrieval, and getting the current time in different timezones. The agent interacts with custom tools like my_custom_tool and get_current_time_in_timezone to perform tasks based on user input. The agent's capabilities include:

Searching the web for events in specified cities and years.
Fetching the current local time in any timezone.

Features
Web Search: The agent can fetch important events based on specific cities and years.
Time Zone Support: Retrieve the current local time for any given timezone.
Simple Integration: Built with Gradio for easy deployment and interaction.

The agent allows you to input a specific query or task, such as:
Fetch events for Paris in 2023:
Input: "Fetch important events in Paris for the year 2023."
Get current time in New York:
Input: "What is the current time in New York?"
