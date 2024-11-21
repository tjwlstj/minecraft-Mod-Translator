# Minecraft Mod Translator  
**(부제)** 영어가 부족해서 만든 모드 번역기
# 아직 개발중입니다. 에러가 있으니 개발자분이 아니라면 사용하지 말아주세요.
---

## 📌 개요
1. **OpenAI의 ChatGPT**를 활용하여 기존 번역기를 개선한 버전입니다.  
2. 이전에 사용하던 `Papago AI`는 가격 부담(약 5달러 + 부가세 0.5달러)으로 인해, **ChatGPT API**로 전환했습니다.
3. **Papago 버전**과 동일하게 **API 키**가 필요하며, OpenAI API를 활용합니다.
4. **API 키 발급 및 레퍼런스**는 [OpenAI API Platform](https://platform.openai.com/)에서 확인할 수 있습니다.
5. **Minecraft 1.18.x ~ 1.21 Forge 모드**에서 테스트를 진행했습니다.
6. `.json` 형태의 `lang` 파일을 포함한 모드는 번역이 가능합니다.

---

## 💾 Requirements (필수 설치 라이브러리)
1. **commentjson**  
   일부 모드 제작자가 JSON에 주석을 추가하는 경우가 있어 필요합니다.  
    ```bash
    pip install commentjson
    ```
2. **openai**
    ```bash
    pip install openai==1.54.4
    ```
## 🚀 사용 방법
1. **`mod` 폴더**를 생성하거나, 프로그램을 한 번 실행하면 자동으로 `mod` 폴더가 생성됩니다.  
   생성된 폴더에 번역할 모드(`.JAR` 파일)를 추가합니다.

2. **API 키 입력**:  
   `Translator.py` 파일을 열어 본인의 **API_KEY**를 입력합니다.  
   OpenAI API 키는 [OpenAI API Platform](https://platform.openai.com/)에서 발급받을 수 있습니다.

3. **명령어 실행**:  
   터미널에서 아래 명령어를 실행합니다.  
   ```bash
   python main.py
   ```

4. 번역 작업은 시간이 다소 소요됩니다.
5. 작업이 완료되면 `translated`**폴더**에 모드파일이 생성됩니다.
6. 번역된 모드 파일을 `마인크래프트 게임 폴더`에 넣고 실행하면 됩니다.
# 🖼️ 스크린샷
![0](./mdimg/01.png)
# 💡 여담
1. 이전 버전들은 혹시몰라 그대로 놔두겠습니다.
2. OpenAI ChatGPT 버전은 테스트 버전입니다.
3. 현재 다른 환경에서 프로그래밍된 코드라 백업 느낌으로 올린거니 실사용하는데 많은 불편함이 있을겁니다. 양해 부탁드립니다. 🙏
