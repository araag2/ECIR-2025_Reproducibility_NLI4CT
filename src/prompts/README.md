# Prompts Detailing

## Short Prompt Structure
    ```
    You are a helpful assistant.
    
    Evidence:
    
    Primary Trial:
    $primary_evidence
    
    Secondary Trial:
    $secondary_evidence
    
    Statement: $hypothesis
    
    Question: Answer in 1 word (Yes or No). Is the statement entailed by the Evidence?
    Answer: "
    ```

## Long Prompt Structure

    ```
    The objective is to examine semantic entailment relationships between individual sections of Clinical Trial Reports (CTRs) and statements articulated by clinical domain experts. CTRs elaborate on the procedures and findings of clinical trials, scrutinizing the effectiveness and safety of novel treatments. Each trial involves cohorts or arms exposed to distinct treatments or exhibiting diverse baseline characteristics. Comprehensive CTRs comprise four sections: (1) ELIGIBILITY CRITERIA delineating conditions for patient inclusion, (2) INTERVENTION particulars specifying type, dosage, frequency, and duration of treatments, (3) RESULTS summary encompassing participant statistics, outcome measures, units, and conclusions, and (4) ADVERSE EVENTS cataloging signs and symptoms observed. Statements posit claims regarding the information within these sections, either for a single CTR or in comparative analysis of two. To establish entailment, the statement's assertion should harmonize with clinical trial data, find substantiation in the CTR, and avoid contradiction with the provided descriptions.
    
    The following descriptions correspond to the information in one of the Clinical Trial Report (CTR) sections.
    
    Primary Trial:
    $primary_evidence
    
    Secondary Trial:
    $secondary_evidence
    
    Statement: $hypothesis
    
    Question: Respond with either YES or NO to indicate whether it is possible to determine the statement's validity based on the Clinical Trial Report (CTR) information, with the statement being supported by the CTR data and not contradicting the provided descriptions.
    Answer: "
    ```