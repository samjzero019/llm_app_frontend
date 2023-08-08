Gen-AI Solution: Frontend Streamlit Application
Welcome to the Gen-AI solution frontend repository! This Streamlit application serves as a user-friendly interface to interact with the powerful Gen-AI solution implementation. With this application, users can effortlessly pose questions and retrieve answers through the utilization of the /llm/rag REST API endpoint provided by the Lambda function.

Getting Started
Follow these steps to quickly set up the Gen-AI frontend application and start exploring the capabilities of our solution:

Step 1: Clone the Repository
Begin by cloning this repository to your local environment and navigating into the project directory:

bash
Copy code
git clone https://github.com/samjzero019/llm_app_frontend.git
cd llm_app_frontend
Step 2: Install Dependencies
Install the necessary Python packages required for the application using pip:

bash
Copy code
pip install -r requirements.txt
Step 3: Configure API Gateway Endpoint
In order to establish a connection between the application and the Gen-AI backend, you'll need to specify the API Gateway endpoint URL provided by the CloudFormation stack output. Open the webapp.py file and locate the line containing **API_GW_ENDPOINT**. Replace this placeholder value with the actual API Gateway endpoint URL obtained from the CloudFormation output.

Example:

python
Copy code
API_GATEWAY_ENDPOINT = "https://your-api-gateway-url.com"
Step 4: Launch the Application
You're all set! To run the Gen-AI frontend application, execute the following command:

bash
Copy code
streamlit run webapp.py
This command will launch the Streamlit application in your default web browser, allowing you to seamlessly interact with the Gen-AI solution.

Additional Information
For more details about the Gen-AI solution, backend implementation, and API usage, please refer to the official documentation and resources provided in the Gen-AI GitHub repository.

We hope you enjoy using our Gen-AI solution frontend to explore and harness the power of artificial intelligence for your questions and inquiries! If you have any questions or encounter any issues, please don't hesitate to reach out to our support team at support@gen-ai.com.

Happy questioning! 🧠🤖
