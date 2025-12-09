import streamlit as st
import google.generativeai as genai
GOOGLE_API_KEY=""
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def main():
    st.set_page_config(page_title="SQL QUERY GENERATOR")
    st.markdown(
        """
         <div style="text-align:center;">
             <h1>SQL QUERY GENERATOR</h1>
             <h3>I can generate SQL queries for you.</h3>
             <h4>With Explanation as well !!!</h4>
             
         </div>
        """,
        unsafe_allow_html=True,
    )
    text_input=st.text_area("Enter Your Prompt Here")
    submit=st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                 create a SQL query snippet using the below text:
                 ```
                 {text_input}
                 ```
                 I just want a SQL Query.



            """
            formatted_template=template.format(text_input=text_input)
            
            response=model.generate_content(formatted_template)
            sql_query=response.text
            sql_query=sql_query.strip().lstrip("```sql").rstrip("```")
            

            expected_output="""
                 what would be the expected output of the below SQL Query:
                 ```
                 {sql_query}
                 ```
                  provide sample tabular response with no explanation



            """
            expected_output_formatted=expected_output.format(sql_query=sql_query)
            eoutput=model.generate_content(expected_output_formatted)
            eoutput=eoutput.text
            

            explanation="""
                 Expalin this sql query
                 ```
                 {sql_query}
                 ```
                  provide with simple explanation



            """
            explanation_formatted=explanation.format(sql_query=sql_query)
            explanation_output=model.generate_content(explanation_formatted)
            explanation_output=explanation_output.text

            with st.container():
                st.success(" SQL Query Generated Successfully ! Here is your Query Below:")
                st.code(sql_query,language="sql")
                st.success("Expected Output of this SQL Query will be :")
                st.markdown(eoutput)
                st.success("Explanation of this SQL Query:")
                st.markdown(explanation_output)
           





            

        
 
        

main()    