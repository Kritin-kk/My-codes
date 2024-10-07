using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    [SerializeField]
    private bool _isgameover;

    private void Update()
    {
        if(Input.GetKeyDown(KeyCode.R) && _isgameover == true)
        {
            SceneManager.LoadScene(1);//current game scene
        }

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Application.Quit();
        }
    }

    public void GameOver()
    {
        _isgameover = true;

    }
}
