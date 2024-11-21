import styles from './TranslationPage.css';
export default function TranslationPage() {
    const randomPhrase = "Ola mundo"


    return (
      <div className={styles.webPage}>
          <h1>Translation Page</h1>
          <p> Este website tem como objetivo, recolher corpora de forma a treinar um modelo de língua para crioulo de
              Cabo Verde</p>

          <form>
              <label>
                  {randomPhrase}
                  <input type="text" name="frase"/>
              </label>
              <input type="submit" value="Submit"/>
          </form>
      </div>
  );
}