# 財務工程相關程式碼

## 主要內容

衍生性金融商品的定價與分析。

## 目前已有專案

### 定價 (資料夾: Pricing)

1. **歐式買權 - 蒙地卡羅**
   - 使用蒙地卡羅計算歐式買權價格，並用 Black-Scholes model 驗證。
   - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/Pricing/%E6%AD%90%E5%BC%8F%E8%B2%B7%E6%AC%8A%20-%20%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85.ipynb)

2. **美式選擇權 - CRR**
   - 使用二元樹(CRR)對美式選擇權進行定價。
   - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/Pricing/%E7%BE%8E%E5%BC%8F%E9%81%B8%E6%93%87%E6%AC%8A%20-%20CRR.ipynb)

3. **重設選擇權 - CRR**
   - 使用二元樹(CRR)對重設選擇權進行定價(歐美式的買賣權)。
   - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/Pricing/%E9%87%8D%E8%A8%AD%E9%81%B8%E6%93%87%E6%AC%8A%20-%20CRR.ipynb)

4. **障礙選擇權**
   - **障礙選擇權 - CRR**
     - 使用二元樹(CRR)對障礙選擇權進行定價(歐美式、上下出局或入局的買賣權)。
     - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/Pricing/%E9%9A%9C%E7%A4%99%E9%81%B8%E6%93%87%E6%AC%8A/%E9%9A%9C%E7%A4%99%E9%81%B8%E6%93%87%E6%AC%8A%20-%20CRR.ipynb)
   - **障礙選擇權 - 蒙地卡羅**
     - 使用蒙地卡羅模擬股價路徑進行障礙選擇權定價。
     - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/Pricing/%E9%9A%9C%E7%A4%99%E9%81%B8%E6%93%87%E6%AC%8A/%E9%9A%9C%E7%A4%99%E9%81%B8%E6%93%87%E6%AC%8A%20-%20%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85.ipynb)

### 分析 

1. **選擇權 - 歷史波動度**
   - 使用實際資料計算某檔股票的歷史波動度。
   - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/%E9%81%B8%E6%93%87%E6%AC%8A%20-%20%E6%AD%B7%E5%8F%B2%E6%B3%A2%E5%8B%95%E5%BA%A6.ipynb)

2. **選擇權 - 隱含波動度**
   - 使用二方法搜尋選擇權當前的隱含波動度。
   - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/%E9%81%B8%E6%93%87%E6%AC%8A%20-%20%E9%9A%B1%E5%90%AB%E6%B3%A2%E5%8B%95%E5%BA%A6.ipynb)

3. **選擇權 - 敏感度分析**
   - 在 Black-Scholes model 下分析選擇權5個敏感度指標對買賣權的影響。
   - [程式碼](https://github.com/RPing16/Financial-Engineering/blob/main/%E9%81%B8%E6%93%87%E6%AC%8A/%E9%81%B8%E6%93%87%E6%AC%8A%20-%20%E6%95%8F%E6%84%9F%E5%BA%A6%E5%88%86%E6%9E%90.ipynb)
