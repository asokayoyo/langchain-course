import datetime
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_ollama import ChatOllama

# Load environment variables from a .env file
load_dotenv()


def main():
    print("Hello from langchain-course!")
    # api_key = os.getenv("OPENAI_API_KEY")
    # print(f"OpenAI API key is set. {api_key}")
    # os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    information = """
    Donald John Trump (born June 14, 1946) is an American politician, media personality, and businessman who is the 47th president of the United States. A member of the Republican Party, he served as the 45th president from 2017 to 2021.

    Born into a wealthy New York City family, Trump graduated from the University of Pennsylvania in 1968 with a bachelor's degree in economics. He became the president of his family's real estate business in 1971, renamed it the Trump Organization, and began acquiring and building skyscrapers, hotels, casinos, and golf courses. He also launched side ventures, many licensing the Trump name, and filed for six business bankruptcies in the 1990s and 2000s. From 2004 to 2015, he hosted the reality television show The Apprentice, bolstering his fame as a billionaire. Presenting himself as a political outsider, Trump won the 2016 presidential election against Democratic Party nominee Hillary Clinton.

    During his first presidency, Trump imposed a travel ban on seven Muslim-majority countries, expanded the Mexico–United States border wall, and enforced a family separation policy on the border. He rolled back environmental and business regulations, signed the Tax Cuts and Jobs Act, and appointed three Supreme Court justices. In foreign policy, Trump withdrew the U.S. from agreements on climate, trade, and Iran's nuclear program, and initiated a trade war with China. In response to the COVID-19 pandemic from 2020, he downplayed its severity, contradicted health officials, and signed the CARES Act. After losing the 2020 presidential election to Joe Biden, Trump attempted to overturn the result, culminating in the January 6 Capitol attack in 2021. He was impeached in 2019 for abuse of power and obstruction of Congress, and in 2021 for incitement of insurrection; the Senate acquitted him both times.

    In 2023, Trump was found liable in civil cases for sexual abuse and defamation and for business fraud. He was found guilty in 34 counts of falsifying business records in 2024, making him the first U.S. president convicted of a felony. After winning the 2024 presidential election against then-vice president Kamala Harris, he was sentenced to a discharge, and two felony indictments against him for retention of classified documents and obstruction of the 2020 election were dismissed without prejudice.

    Trump began his second presidency by initiating mass layoffs of federal workers. He imposed tariffs on nearly all countries at the highest level since the Great Depression and signed the One Big Beautiful Bill Act. His administration's actions—including the targeting of political opponents and civil society, the persecution of transgender people, the mass deportation of immigrants, and the extensive use of executive orders—have drawn over 300 lawsuits challenging their legality.

    Since 2015, Trump's leadership style and political agenda—often referred to as Trumpism—have reshaped the Republican Party's identity. Many of his comments and actions have been characterized as racist or misogynistic. He has made many false or misleading statements during his campaigns and presidency, to a degree unprecedented in American politics. He promotes conspiracy theories. Trump's actions, especially in his second term, have been described as authoritarian and contributing to democratic backsliding. After his first term, scholars and historians ranked him as one of the worst presidents in American history.
    """
    summary_template = """
    Given the following information {information} about a person, provide a concise summary in two sentences:
    1. A short summary of who they are.
    2. Two interesting facts about them.
    """
    summary_prompt_template = ChatPromptTemplate.from_template(summary_template)
    
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    # llm = ChatOllama(model="gpt-oss:latest", temperature=0)
    
    chain = summary_prompt_template | llm
    print(f"Invoking summary chain...{datetime.datetime.now()}")
    response = chain.invoke(input={"information": information})
    print(f"Response received at {datetime.datetime.now()}:")
    print(response.content)

if __name__ == "__main__":
    main()
