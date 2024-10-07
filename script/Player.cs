using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class Player : MonoBehaviour
{

    [SerializeField]
    private float _speed = 3.5f;

    [SerializeField]
    private float _speedmultiplier = 2.0f;

    [SerializeField]
    private GameObject _laserPrefab;

    [SerializeField] 
    private GameObject _tripleshotPrefab;

    [SerializeField]
    private float _fireRate = 0.5f;

    private float _nextFire = 0.0f;

    [SerializeField]
    private int _lives = 3;

    private SpawnManager _spawnManager;

    private bool _istripleshotactive = false;

    private bool _isspeedactive = false;

    private bool _isshieldactive = false;

    [SerializeField]
    private GameObject _shieldVisualiser;

    [SerializeField]
    private int _score;

    [SerializeField]
    private GameObject _rightEngine;

    [SerializeField]
    private GameObject _leftEngine;

    [SerializeField]
    private AudioClip _lasershotSound;

    private AudioSource _audioSource;

    private UIManager _uiManager;

    private Rigidbody2D _rigidbody;


    [SerializeField]
    public InputActionReference fire;



    void Start()
    {

        transform.position = new Vector3(0, 0, 0);
        _spawnManager = GameObject.Find("SpawnManager").GetComponent<SpawnManager>();
        _uiManager = GameObject.Find("Canvas").GetComponent<UIManager>();
        _audioSource = GetComponent<AudioSource>();
        

        if (_spawnManager == null)
        {
            Debug.LogError("Spawn manager is null");

        }

        if(_uiManager == null)
        {
            Debug.LogError("The UiManager is NULL");
        }

        if (_audioSource == null)
        {
            Debug.LogError("The Audio Source on player is NULL");
        }
        else
        {
            _audioSource.clip = _lasershotSound;
        }
    }

    void Update()
    {
        CalcMovement();


        //if (Input.GetKeyDown(KeyCode.Space) && Time.time > _nextFire)
        //{
        //    LaserShoot();
        //}
         

    }

    void CalcMovement()
    {
        //float horizontalinput = Input.GetAxis("Horizontal");

        //float verticalinput = Input.GetAxis("Vertical");

        //Vector3 direction = new Vector3(horizontalinput, verticalinput, 0);

        //transform.Translate(direction * _speed * Time.deltaTime);
        

        if (transform.position.y >= 8)
        {
            transform.position = new Vector3(transform.position.x, -6, 0);
        }
        else if (transform.position.y <= -6)
        {
            transform.position = new Vector3(transform.position.x, 8, 0);
        }

        if (transform.position.x >= 12)
        {
            transform.position = new Vector3(-12, transform.position.y, 0);
        }

        else if (transform.position.x <= -12)
        {
            transform.position = new Vector3(12, transform.position.y, 0);
        }
    }

    //void LaserShoot(InputAction.CallbackContext obj)
    //{

    //    _nextFire = Time.time + _fireRate;

    //    if (_istripleshotactive == true)
    //    {
    //        Instantiate(_tripleshotPrefab, transform.position, Quaternion.identity);

    //    }
    //    else
    //    {
    //        Instantiate(_laserPrefab, transform.position + new Vector3(0, 1.05f, 0), Quaternion.identity);
    //    }

    //    _audioSource.Play();

    //}

    public void Damage()
    {
        if(_isshieldactive == true)
        {
            _shieldVisualiser.gameObject.SetActive(false);
            _isshieldactive = false;
            return;
        }

        _lives -= 1;

        if(_lives == 2)
        {
            _leftEngine.SetActive(true);
        }
        else if (_lives == 1)
        {
            _rightEngine.SetActive(true);
        }

        _uiManager.updateLives(_lives);

        if (_lives < 1)
        {
            _spawnManager.OnPlayerDeath();
            Destroy(this.gameObject);
        }
    }

    public void Tripleshotactive()
    {
        _istripleshotactive = true;
        StartCoroutine(TripleShotpowerdownRoutine());

    }

    IEnumerator TripleShotpowerdownRoutine()
    {
        yield return new WaitForSeconds(5.0f);
        _istripleshotactive = false;
    }

    public void SpeedboostActive()
    {
        _isspeedactive = true;
        _speed *= _speedmultiplier;
        StartCoroutine(SpeedBoostPowerdownRoutine());
    }

    IEnumerator SpeedBoostPowerdownRoutine()
    {
        yield return new WaitForSeconds(5);
        _isspeedactive = false;
        _speed /= _speedmultiplier;
    }

    public void ShieldsActive()
    {
        _isshieldactive = true;
        _shieldVisualiser.gameObject.SetActive(true);
    }

    public void AddScore(int points)
    {
        _score += points;
        _uiManager.UpdateScore(_score);
    }

    private void Awake()
    {
        _rigidbody = GetComponent<Rigidbody2D>();
        if (_rigidbody == null)
        {
            Debug.LogError("Rigidbody2D component is missing!");
        }
    }

    public void OnMove(InputAction.CallbackContext ctx)
    {

        _rigidbody.velocity = ctx.ReadValue<Vector2>() * _speed;

    }

    //public void OnEnable()
    //{
    //    fire.action.started += LaserShoot;
    //}

    public void OnEnable()
    {
        if (fire != null && fire.action != null)
        {
            fire.action.started += LaserShoot;
        }
        else
        {
            Debug.LogError("fire or fire.action is null in OnEnable");
        }
    }

    public void OnDisable()
    {
        if (fire != null && fire.action != null)
        {
            fire.action.started -= LaserShoot;
        }
    }

    void LaserShoot(InputAction.CallbackContext obj)
    {

        _nextFire = Time.time + _fireRate;

        if (_istripleshotactive == true)
        {
            Instantiate(_tripleshotPrefab, transform.position, Quaternion.identity);

        }
        else
        {
            Instantiate(_laserPrefab, transform.position + new Vector3(0, 1.05f, 0), Quaternion.identity);
        }

        _audioSource.Play();

    }
} 