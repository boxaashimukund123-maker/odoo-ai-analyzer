import streamlit as st
        # SMART AI SECTION
        # ============================================

        st.subheader("💬 Ask AI About Your Business Data")

        question = st.text_input(
            "Ask anything about your ERP data..."
        )

        if question:

            q = question.lower()

            if "top" in q or "best" in q:
                st.success(
                    f"{top_product} is the best-performing product "
                    f"with sales of {top_sales}."
                )

            elif "worst" in q or "lowest" in q:
                st.error(
                    f"{worst_product} is the lowest-performing product "
                    f"with sales of {worst_sales}."
                )

            elif "summary" in q:
                st.info(
                    f"Total sales are {total_sales}. "
                    f"{top_product} contributes the highest revenue."
                )

            elif "average" in q:
                st.info(
                    f"The average sales per product is {avg_sales}."
                )

            elif "recommend" in q or "improve" in q:
                st.warning(
                    f"The company should improve sales strategies "
                    f"for {worst_product} and focus more on "
                    f"high-performing products like {top_product}."
                )

            elif "forecast" in q or "prediction" in q:
                st.info(
                    f"AI predicts approximately {predicted_sales} "
                    f"in sales next month with a projected "
                    f"{growth_percent}% growth."
                )

            elif "health" in q:
                st.info(
                    f"Current business health score is {health_score}%."
                )

            else:
                st.info(
                    "Try asking about:\n"
                    "- top products\n"
                    "- worst products\n"
                    "- sales summary\n"
                    "- recommendations\n"
                    "- forecast\n"
                    "- health score"
                )

    else:
        st.info("📁 Upload a CSV file to start analyzing your ERP data.")