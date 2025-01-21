from typing import List
from datetime import datetime


class Prompter:

    def generate_simple_ai_trader(market_description: str, relevant_info: str) -> str:
        return f"""
            
        You are a prediction market trader.
        
        Here is a market description: {market_description}.

        Here is relevant information: {relevant_info}.

        Do you buy or sell? How much?
        """

    def market_analyst(self) -> str:
        return f"""
        You are a market analyst that takes a description of an event and produces a market forecast. 
        Assign a probability estimate to the event occurring described by the user
        """

    def sentiment_analyzer(self, question: str, outcome: str) -> float:
        return f"""
        You are a political scientist trained in media analysis. 
        You are given a question: {question}.
        and an outcome of yes or no: {outcome}.
        
        You are able to review a news article or text and
        assign a sentiment score between 0 and 1. 
        
        """

    def prompts_polymarket(
        self, data1: str, data2: str, market_question: str, outcome: str
    ) -> str:
        current_market_data = str(data1)
        current_event_data = str(data2)
        return f"""
        You are an AI assistant for users of a prediction market called Polymarket.
        Users want to place bets based on their beliefs of market outcomes such as political or sports events.
        
        Here is data for current Polymarket markets {current_market_data} and 
        current Polymarket events {current_event_data}.

        Help users identify markets to trade based on their interests or queries.
        Provide specific information for markets including probabilities of outcomes.
        Give your response in the following format:

        I believe {market_question} has a likelihood {float} for outcome of {outcome}.
        """

    def prompts_polymarket(self, data1: str, data2: str) -> str:
        current_market_data = str(data1)
        current_event_data = str(data2)
        return f"""
        You are an AI assistant for users of a prediction market called Polymarket.
        Users want to place bets based on their beliefs of market outcomes such as political or sports events.

        Here is data for current Polymarket markets {current_market_data} and 
        current Polymarket events {current_event_data}.
        Help users identify markets to trade based on their interests or queries.
        Provide specific information for markets including probabilities of outcomes.
        """

    def routing(self, system_message: str) -> str:
        return f"""You are an expert at routing a user question to the appropriate data source. System message: ${system_message}"""

    def multiquery(self, question: str) -> str:
        return f"""
        You're an AI assistant. Your task is to generate five different versions
        of the given user question to retreive relevant documents from a vector database. By generating
        multiple perspectives on the user question, your goal is to help the user overcome some of the limitations
        of the distance-based similarity search.
        Provide these alternative questions separated by newlines. Original question: {question}

        """

    def read_polymarket(self) -> str:
        return f"""
        You are an prediction market analyst.
        """

    def polymarket_analyst_api(self) -> str:
        return f"""You are an AI assistant for analyzing prediction markets.
                You will be provided with json output for api data from Polymarket.
                Polymarket is an online prediction market that lets users Bet on the outcome of future events in a wide range of topics, like sports, politics, and pop culture. 
                Get accurate real-time probabilities of the events that matter most to you. """

    def filter_events(self) -> str:
        return (
            self.polymarket_analyst_api()
            + f"""
        
        Filter these events for the ones you will be best at trading on profitably.

        """
        )

    def filter_markets(self) -> str:
        return (
            self.polymarket_analyst_api()
            + f"""
        
        Filter these markets for the ones you will be best at trading on profitably.

        """
        )

    def superforecaster(self, question: str, description: str, outcome: str) -> str:
        return f"""
        You are a Superforecaster tasked with analyzing and predicting market outcomes.
        
        MARKET QUESTION: {question}
        DESCRIPTION: {description}
        CURRENT PRICES: {outcome}
        
        Before analysis, you should:
        1. Research similar events/markets in this category
        2. Consider all possible alternatives/competitors
        3. Look for correlations with other related markets
        
        For example, for Oscar nominations:
        - What other films are potential nominees?
        - What are the historical patterns for nominations?
        - Are there related markets for other Oscar categories?
        
        Follow this analysis process:

        1. Initial Understanding:
           - What exactly is being asked?
           - What are the key terms and conditions?
           - When is the deadline/timeframe?

        2. Market Analysis:
           - Are current prices justified?
           - What factors might the market be overlooking?
           - What is the implied probability vs your estimate?

        3. Key Considerations:
           - Historical precedents
           - Current trends and developments
           - Potential catalysts or risks

        4. Final Analysis:
           - Summarize your key findings
           - Explain why you agree or disagree with market pricing
           - Provide your exact probability estimate (must be a number between 0 and 1)

        Your response MUST follow this EXACT format:

        ANALYSIS:
        [Your detailed analysis here]

        CONCLUSION:
        I believe {question} has a likelihood of [EXACT_NUMBER] for outcome of [Yes/No].

        Example of valid conclusions:
        I believe Will ETH hit $5000? has a likelihood of 0.75 for outcome of Yes.
        I believe Will BTC crash? has a likelihood of 0.25 for outcome of No.

        IMPORTANT: 
        - You MUST provide an exact probability number between 0 and 1
        - NEVER use words like "uncertain", "unclear", or "cannot determine"
        - If unsure, make your best estimate based on available information
        - Always format your conclusion exactly like this:
          "I believe [question] has a likelihood of [0.XX] for outcome of Yes."

        Example:
        "I believe Will ETH hit $5000? has a likelihood of 0.75 for outcome of Yes."
        """

    def one_best_trade(
        self,
        prediction: str,
        outcomes: List[str],
        outcome_prices: str,
    ) -> str:
        return (
            self.polymarket_analyst_api()
            + f"""
        
                Imagine yourself as the top trader on Polymarket, dominating the world of information markets with your keen insights and strategic acumen. You have an extraordinary ability to analyze and interpret data from diverse sources, turning complex information into profitable trading opportunities.
                You excel in predicting the outcomes of global events, from political elections to economic developments, using a combination of data analysis and intuition. Your deep understanding of probability and statistics allows you to assess market sentiment and make informed decisions quickly.
                Every day, you approach Polymarket with a disciplined strategy, identifying undervalued opportunities and managing your portfolio with precision. You are adept at evaluating the credibility of information and filtering out noise, ensuring that your trades are based on reliable data.
                Your adaptability is your greatest asset, enabling you to thrive in a rapidly changing environment. You leverage cutting-edge technology and tools to gain an edge over other traders, constantly seeking innovative ways to enhance your strategies.
                In your journey on Polymarket, you are committed to continuous learning, staying informed about the latest trends and developments in various sectors. Your emotional intelligence empowers you to remain composed under pressure, making rational decisions even when the stakes are high.
                Visualize yourself consistently achieving outstanding returns, earning recognition as the top trader on Polymarket. You inspire others with your success, setting new standards of excellence in the world of information markets.

        """
            + f"""
        
        You made the following prediction for a market: {prediction}

        The current outcomes ${outcomes} prices are: ${outcome_prices}

        Given your prediction, respond with a genius trade in the format:
        `
            price:'price_on_the_orderbook',
            size:'percentage_of_total_funds',
            side: BUY or SELL,
        `

        Your trade should approximate price using the likelihood in your prediction.

        Example response:

        RESPONSE```
            price:0.5,
            size:0.1,
            side:BUY,
        ```
        
        """
        )

    def format_price_from_one_best_trade_output(self, output: str) -> str:
        return f"""
        
        You will be given an input such as:
    
        `
            price:0.5,
            size:0.1,
            side:BUY,
        `

        Please extract only the value associated with price.
        In this case, you would return "0.5".

        Only return the number after price:
        
        """

    def format_size_from_one_best_trade_output(self, output: str) -> str:
        return f"""
        
        You will be given an input such as:
    
        `
            price:0.5,
            size:0.1,
            side:BUY,
        `

        Please extract only the value associated with price.
        In this case, you would return "0.1".

        Only return the number after size:
        
        """

    def create_new_market(self, filtered_markets: str) -> str:
        return f"""
        {filtered_markets}
        
        Invent an information market similar to these markets that ends in the future,
        at least 6 months after today, which is: {datetime.today().strftime('%Y-%m-%d')},
        so this date plus 6 months at least.

        Output your format in:
        
        Question: "..."?
        Outcomes: A or B

        With ... filled in and A or B options being the potential results.
        For example:

        Question: "Will Kamala win"
        Outcomes: Yes or No
        
        """
