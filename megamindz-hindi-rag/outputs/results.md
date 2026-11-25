# MegaMindz Level 1 RAG — Test Query Results

## Query 1 (HI)
- **Query:** SLV-III ने किस उपग्रह को कक्षा में स्थापित किया और किस वर्ष?
- **Answer:** दिए गए संदर्भ के अनुसार:

SLV-III ने **रोहिणी उपग्रह** को **जुलाई 1980** में सफलतापूर्वक कक्षा में स्थापित किया।
- **Model:** gemini-3.6-flash
- **Primary Citation:** page: 8, section: "20. त्वरित तथ्य-सारांश", chunk_id: chunk_0027, score: 0.6047
- **All Retrieved Chunks:**
  - page: 8 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0027 | score: 0.6047
  - page: 8 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0029 | score: 0.5828
  - page: 17 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0055 | score: 0.5351
  - page: 17 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0056 | score: 0.5292
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0064 | score: 0.5179

## Query 2 (HI)
- **Query:** कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?
- **Answer:** दिए गए संदर्भ के अनुसार, कलाम को **1997** में भारत रत्न प्राप्त हुआ।
- **Model:** gemini-3.6-flash
- **Primary Citation:** page: 21, section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?", chunk_id: chunk_0066, score: 0.6702
- **All Retrieved Chunks:**
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0066 | score: 0.6702
  - page: 16 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0053 | score: 0.6448
  - page: 20 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0063 | score: 0.6432
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0065 | score: 0.6424
  - page: 14 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0047 | score: 0.5769

## Query 3 (HI)
- **Query:** पोखरण-II में कलाम की क्या भूमिका थी?
- **Answer:** दिए गए संदर्भ (chunk_0034) के अनुसार:

पोखरण-II (मई 1998 के परमाणु परीक्षणों) के समय कलाम **रक्षा मंत्री के वैज्ञानिक सलाहकार** तथा **डीआरडीओ (DRDO) के प्रमुख** के रूप में सेवारत थे। उन्होंने परमाणु ऊर्जा विभाग के वैज्ञानिकों के साथ मिलकर एक **केंद्रीय संगठनात्मक भूमिका** निभाई।
- **Model:** gemini-3.6-flash
- **Primary Citation:** page: 20, section: "5. उदाहरण और उपस्थि", chunk_id: chunk_0063, score: 0.6029
- **All Retrieved Chunks:**
  - page: 20 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0063 | score: 0.6029
  - page: 10 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0034 | score: 0.602
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0065 | score: 0.5473
  - page: 2 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0004 | score: 0.5012
  - page: 14 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0049 | score: 0.4913

## Query 4 (EN)
- **Query:** Which institution did Kalam attend to study aeronautical engineering?
- **Answer:** Based on the provided context, Abdul Kalam attended the **Madras Institute of Technology (MIT)** in Chennai (मद्रास इंस्टीट्यूट ऑफ टेक्नोलॉजी, चेन्नई) to study aeronautical engineering.
- **Model:** gemini-3.6-flash
- **Primary Citation:** page: 6, section: "20. त्वरित तथ्य-सारांश", chunk_id: chunk_0019, score: 0.5687
- **All Retrieved Chunks:**
  - page: 6 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0019 | score: 0.5687
  - page: 20 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0063 | score: 0.537
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0064 | score: 0.5167
  - page: 7 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0023 | score: 0.4796
  - page: 6 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0021 | score: 0.4736

## Query 5 (EN)
- **Query:** Who co-wrote the autobiography, and in what year was it published?
- **Answer:** Based on the provided context, the autobiography (*अग्नि की उड़ान*) was co-written with scientist **Arun Tiwari** (वैज्ञानिक अरुण तिवारी) and was published in the year **1999**.
- **Model:** gemini-3.6-flash
- **Primary Citation:** page: 3, section: "20. त्वरित तथ्य-सारांश", chunk_id: chunk_0009, score: 0.5577
- **All Retrieved Chunks:**
  - page: 3 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0009 | score: 0.5577
  - page: 3 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0008 | score: 0.5333
  - page: 1 | section: "शीर्षक / भूमिका" | chunk_id: chunk_0001 | score: 0.4717
  - page: 1 | section: "शीर्षक / भूमिका" | chunk_id: chunk_0002 | score: 0.4365
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0065 | score: 0.4284

## Query 6 (EN)
- **Query:** How and where did Kalam die in 2015?
- **Answer:** Based on the provided context, Dr. A.P.J. Abdul Kalam passed away in **Shillong, Meghalaya** (specifically at the **Indian Institute of Management Shillong**). 

He died after **collapsing while delivering a lecture to students** on July 27, 2015, and passed away shortly after at the age of 83.
- **Model:** gemini-3.6-flash
- **Primary Citation:** page: 15, section: "5. उदाहरण और उपस्थि", chunk_id: chunk_0052, score: 0.5594
- **All Retrieved Chunks:**
  - page: 15 | section: "5. उदाहरण और उपस्थि" | chunk_id: chunk_0052 | score: 0.5594
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0066 | score: 0.4813
  - page: 22 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0067 | score: 0.4439
  - page: 4 | section: "20. त्वरित तथ्य-सारांश" | chunk_id: chunk_0011 | score: 0.4224
  - page: 21 | section: "12. कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?" | chunk_id: chunk_0065 | score: 0.4166
