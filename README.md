# Gen-AI Solution: Frontend Streamlit Application

Welcome to the Gen-AI solution frontend repository! This Streamlit application serves as a user-friendly interface to interact with the powerful Gen-AI solution implementation. With this application, users can effortlessly pose questions and retrieve answers through the utilization of the /llm/rag REST API endpoint provided by the Lambda function.

## Getting Started

Follow these steps to quickly set up the Gen-AI frontend application and start exploring the capabilities of our solution:

### Step 1: Clone the Repository

Begin by cloning this repository to your local environment and navigating into the project directory:

```bash
git clone https://github.com/samjzero019/llm_app_frontend.git
cd llm_app_frontend
```

### Step 2: Install Dependencies

Install the necessary Python packages required for the application using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Gateway Endpoint

In order to establish a connection between the application and the Gen-AI backend, you'll need to specify the API Gateway endpoint URL provided by the CloudFormation stack output. Follow these instructions to complete the configuration:

1. Open the `webapp.py` file located in the project directory.

2. Locate the line containing the placeholder `__API_GW_ENDPOINT__`.

3. Replace the placeholder value with the actual API Gateway endpoint URL obtained from the CloudFormation output. The line should look like this:

   ```python
   API_GATEWAY_ENDPOINT = "https://your-api-gateway-url.com/env"
   ```

4. Save the `webapp.py` file after making the necessary changes.

### Step 4: Launch the Application

You're all set! To run the Gen-AI frontend application, execute the following command:

```bash
streamlit run webapp.py
```

## Additional Information

We encourage you to explore the repository to gain deeper insights into how the Gen-AI solution works and how you can make the most out of its features. The repository contains comprehensive guides, code examples, and explanations to help you get the best experience.

If you have any questions, suggestions, or encounter any issues while using the Gen-AI solution or this frontend application, please don't hesitate to reach out to our dedicated support team at usama.jameel@netsoltech.com. We are here to assist you every step of the way!

Happy questioning and discovering the power of artificial intelligence with Gen-AI! 🧠🤖
