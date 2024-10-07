using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PowerUp : MonoBehaviour
{

    [SerializeField]
    private float _speed = 3.0f;

    [SerializeField]
    private int powerupid;

    [SerializeField]
    private AudioClip _clip;

    

    // Update is called once per frame
    void Update()
    {
        transform.Translate(Vector3.down * _speed * Time.deltaTime);

        if(transform.position.y < -4.5f)
        {
            Destroy(this.gameObject);
        }

    }

    private void OnTriggerEnter2D(Collider2D other)
    {

        AudioSource.PlayClipAtPoint(_clip, transform.position);

        if(other.tag == "Player")
        {
            Player player = other.transform.GetComponent<Player>();
            if(player != null)
            {
                switch (powerupid)
                {
                    case 0:
                        player.Tripleshotactive();
                        break;
                    case 1:
                        player.SpeedboostActive();
                        break;
                    case 2:
                        player.ShieldsActive();
                        break;
                    default:

                        break;
                }
            }
            Destroy(this.gameObject);
        }
    }
}
