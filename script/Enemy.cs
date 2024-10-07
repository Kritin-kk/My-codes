using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{


    [SerializeField]
    private float _enemyspeed = 4.0f;

    private Player _player;

    private Animator _explosionanim;

    private AudioSource _audiosource;

    // Start is called before the first frame update
    void Start()
    {
        _player = GameObject.Find("Player").GetComponent<Player>();
        _audiosource = GetComponent<AudioSource>();

        if(_player == null)
        {
            Debug.LogError("Player Is null");
        }

        _explosionanim = GetComponent<Animator>();
        if (_explosionanim == null)
        {
            Debug.LogError("Animator Is null");
        }

    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(Vector3.down * _enemyspeed * Time.deltaTime);
        if (transform.position.y <= -6)
        {
            transform.position = new Vector3(Random.Range(-8.0f,8.0f), 5, 0);
        }

    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if(other.tag == "Player")
        {
            Player player = other.transform.GetComponent<Player>();

            if (player != null)
            {
                player.Damage();
            }

            _explosionanim.SetTrigger("onEnemyDeath");
            _enemyspeed = 0;
            _audiosource.Play();
            Destroy(this.gameObject, 2.6f);
            

        }

        if (other.tag == "laser")
        {
            Destroy(other.gameObject);
            if(_player != null)
            {
                _player.AddScore(10);
               
            }
            else
            {
                Debug.LogError("TextMeshProUGUI component not found.");
            }

            _explosionanim.SetTrigger("onEnemyDeath");
            _enemyspeed = 0;
            _audiosource.Play();
            Destroy(this.gameObject, 1.0f);
            
        }
    }

}
