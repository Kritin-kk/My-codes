using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class UIManager : MonoBehaviour
{
    [SerializeField]
    private TextMeshProUGUI _scoreText;

    [SerializeField]
    private TextMeshProUGUI _gameoverText;

    [SerializeField]
    private Image _liveImg;

    [SerializeField]
    private Sprite[] _liveSprites;

    [SerializeField]
    private TextMeshProUGUI _restartText;

    private GameManager _gameManager;



    // Start is called before the first frame update
    void Start()
    {
        _scoreText.text = "Score: " + 0;
        _gameoverText.gameObject.SetActive(false);
        _gameManager = GameObject.Find("Game_Manager").GetComponent<GameManager>();

        if(_gameManager == null)
        {
            Debug.LogError("Game manager is null");
        }
    }

    public void UpdateScore(int player_score)
    {
        _scoreText.text = "Score:" + player_score.ToString();
    }

    public void updateLives(int current_live)
    {
        _liveImg.sprite = _liveSprites[current_live];
        if (current_live == 0)
        {
            gameOverSeq();
        }
    }

    void gameOverSeq()
    {
        _gameManager.GameOver();
        _gameoverText.gameObject.SetActive(true);
        _restartText.gameObject.SetActive(true);
        StartCoroutine(GameOverFlickerRoutine());

    }


    IEnumerator GameOverFlickerRoutine()
    {
        while (true)
        {
            _gameoverText.text = "Game Over";
            yield return new WaitForSeconds(0.5f);
            _gameoverText.text = "";
            yield return new WaitForSeconds(0.5f);

        }
    }


}
