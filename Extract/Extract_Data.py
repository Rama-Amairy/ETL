
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import csv


def inil_driver(Website_link):
    service = Service(ChromeDriverManager().install())
    # Initialize the WebDriver with the Service
    driver = webdriver.Chrome(service=service)
    driver.get(Website_link)
    return driver


def Extract_data_Lexpert(website_link ,output_path):
    driver=inil_driver(website_link)
    # Wait for the page to load
    wait = WebDriverWait(driver, 20)

    while True:
        try:
            # Wait for the "More" button to be clickable
            more_button = wait.until(EC.element_to_be_clickable((By.ID, "btnShowMore")))
            # Scroll to the button to ensure it's visible
            driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
            # Click the button
            more_button.click()
            print("Clicked 'More' button.")
            # Short delay to allow content to load
            time.sleep(2)
        except Exception as e:
            print("No more 'More' button found or an error occurred.")
            break
    
    # Extract all law firm names
    law_firm_elements = driver.find_elements(By.CLASS_NAME, "card-vertical-list-title")

    # Extract and print law firm names
    law_firms = []
    for element in law_firm_elements:
        name = element.text.strip() if element.text.strip() else "No name available"
        link = element.get_attribute('href') if element.get_attribute('href') else "No link available"
        law_firms.append({'Name': name,
            'Link': link})
    df = pd.DataFrame(law_firms, columns=["Name", "Link"])
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
    

#get more data about law firms immigrations in canada

def Extract_data_Best_law_firms(website_link, output_path):
    driver=inil_driver(website_link)
    # Wait for the page to load
    wait = WebDriverWait(driver, 20)

    
# Extract all law firm names
#law_firm_elements = driver.find_elements(By.CLASS_NAME, "p-3")
#text-charcoal text-charcoal-hover d-block position-relative background-light-gray-2-hover
    law_firm_elements2 = wait.until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "text-charcoal.text-charcoal-hover.d-block.position-relative.background-light-gray-2-hover"))
    )


#firm_name_element= driver.find_element(By.CLASS_NAME,"p-3")
# Extract and print law firm names and do some process to text name
    law_firms2 = []
    for element in law_firm_elements2:
        name = element.text.strip() if element.text.strip() else "No name available"
        name = name.split("\n")[0]
        link = element.get_attribute('href') if element.get_attribute('href') else "No link available"
        law_firms2.append({'Name': name,
            'Link': link})
        print(len(law_firms2))
    
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Link"])
        writer.writeheader()
        writer.writerows(law_firms2)

    print(f"Data saved to {output_path}")
    driver.quit()




#Extract  lawyers data in canada
    
def Extract_Lawyers_data(web_link,output_path):
# Wait for the page to load
    driver=inil_driver(web_link)
    wait = WebDriverWait(driver, 20)

    while True:
        try:
            # Wait for the "More" button to be clickable
            more_button = wait.until(EC.element_to_be_clickable((By.ID, "btnShowMore")))
            # Scroll to the button to ensure it's visible
            driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
            # Click the button
            more_button.click()
            print("Clicked 'More' button.")
            # Short delay to allow content to load
            time.sleep(10)

        except Exception as e:
            print("No more 'More' button found or an error occurred.")
        break

    lawyers_data = []

    try:
        lawyer_cards = driver.find_elements(By.CLASS_NAME, 'card-vertical-list__item__passage')  # Update with the actual class name
    
        for card in lawyer_cards:
            # Extract lawyer name
            name = card.find_element(By.CLASS_NAME, 'card-vertical-list-title').text.strip()

            links = card.find_elements(By.TAG_NAME, 'a')

            # Check if any <a> tag is found
            if links:
                link = links[0].get_attribute('href')

            # Extract location/province
            location = card.find_element(By.CLASS_NAME, 'card-vertical-list-area').text.strip()

            # Extract company URL
            company_tag = card.find_element(By.CLASS_NAME,'card-vertical-list-firm').text.strip()
            #company_url = company_tag.get_attribute('href') if company_tag else None

            # Append details to list
            lawyers_data.append({
            'Lawyer name': name,
            'Information Link': link,
            'Location': location,
            'company name': company_tag
           # 'Company URL': company_url
                 })

    except Exception as e:
        print(f"Error during scraping: {e}")
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Lawyer name", "Information Link","Location", "company name"])
        writer.writeheader()
        writer.writerows(lawyers_data)

    print(f"Data saved to {output_path}")


def Extract():
    country=["alberta","british-columbia","manitoba","nova-scotia","ontario","quebec"]
    for x in country:
                website_link = "https://www.bestlawfirms.com/canada/immigration-law/"+x
                output_file = r'C:\Users\asus\Desktop\Law data\Data\province data\law_firms_canada-'+x+'.csv'
                Extract_data_Best_law_firms(website_link=website_link,output_path=output_file)
        
        # 2- firms names work in immigration law in canada
    data_path= r'C:\Users\asus\Desktop\Law data\Data\law_firms_canada.csv'
    Extract_data_Lexpert("https://www.lexpert.ca/rankings/best-law-firm/dir/immigration-law", data_path)

    # 3- Lawyers names work in immigration law in canada
    output_file = r'C:\Users\asus\Desktop\law data\Data\immigration_lawyers.csv'
    website="https://www.lexpert.ca/rankings/best-lawyer/dir/immigration-law"
    Extract_Lawyers_data(web_link=website, output_path=output_file)

if __name__ == "__main__":
               # 3- Lawyers names work in immigration law in canada
    output_file = r'C:\Users\asus\Desktop\law data\Data\immigration_lawyers.csv'
    website="https://www.lexpert.ca/rankings/best-lawyer/dir/immigration-law"
    Extract_Lawyers_data(web_link=website, output_path=output_file)
